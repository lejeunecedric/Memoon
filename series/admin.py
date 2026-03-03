from django.contrib import admin
from .admin_config import *
from .models import (
    Series,
    Season,
    Episode,
    Sequence,
    Shot,
    Character,
    WardrobeItem,
    ShotCharacter,
)


class SeasonInline(admin.TabularInline):
    model = Season
    extra = 1
    fields = ["number", "title"]


class EpisodeInline(admin.TabularInline):
    model = Episode
    extra = 1
    fields = ["number", "title"]


class SequenceInline(admin.TabularInline):
    model = Sequence
    extra = 1
    fields = ["number", "title"]


class ShotInline(admin.TabularInline):
    model = Shot
    extra = 1
    fields = ["number", "script", "background", "camera_angle", "camera_movement"]


class ShotCharacterInline(admin.TabularInline):
    model = ShotCharacter
    extra = 1


class WardrobeItemInline(admin.TabularInline):
    model = WardrobeItem
    extra = 1


@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at", "updated_at"]
    search_fields = ["title", "description"]
    inlines = [SeasonInline]


@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = ["__str__", "number", "series"]
    list_filter = ["series"]
    search_fields = ["title", "series__title"]
    inlines = [EpisodeInline]


@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ["__str__", "number", "season", "script_status", "script_author"]
    list_filter = ["season__series", "season", "script_status"]
    search_fields = ["title", "season__series__title", "script", "script_author"]
    inlines = [SequenceInline]
    fieldsets = [
        (None, {"fields": ["season", "number", "title"]}),
        ("Script", {"fields": ["script", "script_status", "script_author"]}),
        ("Details", {"fields": ["description", "duration"], "classes": ["collapse"]}),
    ]


@admin.register(Sequence)
class SequenceAdmin(admin.ModelAdmin):
    list_display = ["__str__", "number", "episode"]
    list_filter = ["episode__season__series", "episode__season"]
    search_fields = ["title", "episode__title"]
    inlines = [ShotInline]


@admin.register(Shot)
class ShotAdmin(admin.ModelAdmin):
    list_display = ["__str__", "number", "sequence", "background"]
    list_filter = ["sequence__episode__season__series", "sequence__episode__season"]
    search_fields = ["script", "background"]
    inlines = [ShotCharacterInline]
    fieldsets = [
        (None, {"fields": ["sequence", "number"]}),
        ("Script", {"fields": ["script"]}),
        (
            "Visual Elements",
            {"fields": ["background", "camera_angle", "camera_movement"]},
        ),
        ("Additional Info", {"fields": ["duration", "notes"], "classes": ["collapse"]}),
    ]


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]
    search_fields = ["name", "description"]
    filter_horizontal = ["series"]
    inlines = [WardrobeItemInline]


@admin.register(WardrobeItem)
class WardrobeItemAdmin(admin.ModelAdmin):
    list_display = ["__str__", "character"]
    list_filter = ["character"]
    search_fields = ["name", "character__name"]


@admin.register(ShotCharacter)
class ShotCharacterAdmin(admin.ModelAdmin):
    list_display = ["__str__", "shot", "character", "wardrobe"]
    list_filter = ["character", "wardrobe"]
    search_fields = ["shot__script", "character__name"]
