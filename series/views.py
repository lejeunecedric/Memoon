from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView, DetailView, FormView, CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import HttpResponse
from django.conf import settings
import csv
import io
from .models import (
    Series,
    Season,
    Episode,
    Sequence,
    Shot,
    Character,
    WardrobeItem,
    ShotCharacter,
    Prop,
)
from .forms import CSVImportForm
from .exporters.otio_exporter import export_episode


class SeriesListView(ListView):
    model = Series
    template_name = "series/series_list.html"
    context_object_name = "series_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Check if database is empty (fresh setup)
        if not Series.objects.exists():
            context['show_sample_data_prompt'] = True
        return context


class SeriesDetailView(DetailView):
    model = Series
    template_name = "series/series_detail.html"
    context_object_name = "series"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["seasons"] = self.object.seasons.prefetch_related("episodes")
        return context


class SeasonDetailView(DetailView):
    model = Season
    template_name = "series/season_detail.html"
    context_object_name = "season"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["episodes"] = self.object.episodes.prefetch_related("sequences")
        return context


class EpisodeDetailView(DetailView):
    model = Episode
    template_name = "series/episode_detail.html"
    context_object_name = "episode"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sequences"] = self.object.sequences.prefetch_related(
            "shots__characters"
        )
        return context


class SequenceCreateView(CreateView):
    model = Sequence
    fields = ["number", "title", "description"]
    template_name = "series/sequence_form.html"

    def get_success_url(self):
        return reverse_lazy("series:episode_detail", kwargs={"pk": self.kwargs["episode_pk"]})

    def form_valid(self, form):
        episode = get_object_or_404(Episode, pk=self.kwargs["episode_pk"])
        form.instance.episode = episode
        messages.success(self.request, "Sequence added successfully!")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["episode"] = get_object_or_404(Episode, pk=self.kwargs["episode_pk"])
        return context


class SequenceDetailView(DetailView):
    model = Sequence
    template_name = "series/sequence_detail.html"
    context_object_name = "sequence"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["shots"] = self.object.shots.prefetch_related(
            "shotcharacter_set__character", "shotcharacter_set__wardrobe"
        )
        return context


class EpisodeStoryboardView(DetailView):
    """View for displaying sequences as visual cards in a grid layout."""
    model = Episode
    template_name = "series/episode_storyboard.html"
    context_object_name = "episode"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Prefetch shots with images for thumbnail display
        context["sequences"] = self.object.sequences.prefetch_related(
            "shots__characters"
        ).all()
        return context


class SequenceStoryboardView(DetailView):
    """View for displaying shots as visual cards in a grid layout."""
    model = Sequence
    template_name = "series/sequence_storyboard.html"
    context_object_name = "sequence"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Prefetch related data for display
        context["shots"] = self.object.shots.prefetch_related(
            "shotcharacter_set__character", "shotcharacter_set__wardrobe"
        ).all()
        return context


class ShotCreateView(CreateView):
    model = Shot
    fields = ["number", "script", "background", "camera_angle", "camera_movement", "duration", "notes"]
    template_name = "series/shot_form.html"

    def get_success_url(self):
        return reverse_lazy("series:sequence_detail", kwargs={"pk": self.kwargs["sequence_pk"]})

    def form_valid(self, form):
        sequence = get_object_or_404(Sequence, pk=self.kwargs["sequence_pk"])
        form.instance.sequence = sequence
        messages.success(self.request, "Shot added successfully!")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sequence"] = get_object_or_404(Sequence, pk=self.kwargs["sequence_pk"])
        return context


class ShotDetailView(DetailView):
    model = Shot
    template_name = "series/shot_detail.html"
    context_object_name = "shot"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["shot_characters"] = self.object.shotcharacter_set.select_related(
            "character", "wardrobe"
        )
        context["props"] = self.object.props.all()
        return context


class CharacterListView(ListView):
    model = Character
    template_name = "series/character_list.html"
    context_object_name = "characters"

    def get_queryset(self):
        return Character.objects.prefetch_related('series').order_by('series__title', 'name')


class CharacterDetailView(DetailView):
    model = Character
    template_name = "series/character_detail.html"
    context_object_name = "character"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["wardrobe_items"] = self.object.wardrobe_items.all()
        context["shots"] = self.object.shots.select_related(
            "sequence__episode__season__series"
        )[:20]
        return context


class CSVImportView(FormView):
    template_name = "series/csv_import.html"
    form_class = CSVImportForm
    success_url = "/"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["series_queryset"] = Series.objects.all()
        return kwargs

    def form_valid(self, form):
        csv_file = form.cleaned_data["csv_file"]
        series = form.cleaned_data["series"]
        season_number = form.cleaned_data["season_number"]
        episode_number = form.cleaned_data["episode_number"]

        try:
            decoded_file = csv_file.read().decode("utf-8")
            io_string = io.StringIO(decoded_file)
            reader = csv.DictReader(io_string)

            with transaction.atomic():
                season, _ = Season.objects.get_or_create(
                    series=series,
                    number=season_number,
                    defaults={"title": f"Season {season_number}"},
                )
                episode, _ = Episode.objects.get_or_create(
                    season=season,
                    number=episode_number,
                    defaults={"title": f"Episode {episode_number}"},
                )

                shot_count = 0
                for row in reader:
                    sequence_number = int(row.get("sequence_number", 1))
                    shot_number = int(row.get("shot_number", 1))

                    sequence, _ = Sequence.objects.get_or_create(
                        episode=episode,
                        number=sequence_number,
                        defaults={"title": row.get("sequence_title", "")},
                    )

                    shot, created = Shot.objects.get_or_create(
                        sequence=sequence,
                        number=shot_number,
                        defaults={
                            "script": row.get("script", ""),
                            "background": row.get("background", ""),
                            "camera_angle": row.get("camera_angle", ""),
                            "camera_movement": row.get("camera_movement", ""),
                        },
                    )

                    if not created:
                        shot.script = row.get("script", shot.script)
                        shot.background = row.get("background", shot.background)
                        shot.camera_angle = row.get("camera_angle", shot.camera_angle)
                        shot.camera_movement = row.get(
                            "camera_movement", shot.camera_movement
                        )
                        shot.save()

                    characters_str = row.get("characters", "")
                    wardrobe_str = row.get("wardrobe", "")

                    if characters_str:
                        character_names = [
                            name.strip() for name in characters_str.split(",")
                        ]
                        wardrobe_items = (
                            [item.strip() for item in wardrobe_str.split(",")]
                            if wardrobe_str
                            else []
                        )

                        for idx, char_name in enumerate(character_names):
                            if char_name:
                                character, _ = Character.objects.get_or_create(
                                    name=char_name, defaults={"description": ""}
                                )
                                character.series.add(series)

                                wardrobe = None
                                if idx < len(wardrobe_items) and wardrobe_items[idx]:
                                    wardrobe, _ = WardrobeItem.objects.get_or_create(
                                        character=character,
                                        name=wardrobe_items[idx],
                                        defaults={"description": ""},
                                    )

                                ShotCharacter.objects.get_or_create(
                                    shot=shot,
                                    character=character,
                                    defaults={"wardrobe": wardrobe},
                                )

                    shot_count += 1

            messages.success(
                self.request, f"Successfully imported {shot_count} shots into {episode}"
            )

        except Exception as e:
            messages.error(self.request, f"Error importing CSV: {str(e)}")
            return self.form_invalid(form)

        return super().form_valid(form)


def episode_otio_export(request, pk):
    episode = get_object_or_404(
        Episode.objects.prefetch_related(
            "sequences__shots__shotcharacter_set__character",
            "sequences__shots__shotcharacter_set__wardrobe",
        ),
        pk=pk,
    )

    format_type = request.GET.get("format", "otio")
    if format_type not in ("otio", "fcpxml"):
        format_type = "otio"

    media_base_path = request.GET.get("media_path", settings.OTIO_MEDIA_BASE_PATH)
    frame_rate = int(request.GET.get("framerate", settings.OTIO_DEFAULT_FRAMERATE))

    content = export_episode(
        episode,
        format=format_type,
        media_base_path=media_base_path,
        frame_rate=frame_rate,
    )

    extension = "fcpxml" if format_type == "fcpxml" else "otio"
    filename = f"{episode.season.series.title}_S{episode.season.number:02d}E{episode.number:02d}.{extension}"

    response = HttpResponse(
        content,
        content_type="application/xml"
        if format_type == "fcpxml"
        else "application/json",
    )
    response["Content-Disposition"] = f'attachment; filename="{filename}"'

    return response


def login_view(request):
    """Handle user login."""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            next_url = request.GET.get("next", "/")
            return redirect(next_url)
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, "registration/login.html")


def logout_view(request):
    """Handle user logout."""
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("series:series_list")
