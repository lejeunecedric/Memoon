from django.urls import path
from . import views

app_name = "series"

urlpatterns = [
    path("", views.SeriesListView.as_view(), name="series_list"),
    path("series/<int:pk>/", views.SeriesDetailView.as_view(), name="series_detail"),
    path("season/<int:pk>/", views.SeasonDetailView.as_view(), name="season_detail"),
    path("episode/<int:pk>/", views.EpisodeDetailView.as_view(), name="episode_detail"),
    path(
        "episode/<int:pk>/export/otio/",
        views.episode_otio_export,
        name="episode_otio_export",
    ),
    path(
        "sequence/<int:pk>/", views.SequenceDetailView.as_view(), name="sequence_detail"
    ),
    path("shot/<int:pk>/", views.ShotDetailView.as_view(), name="shot_detail"),
    path("characters/", views.CharacterListView.as_view(), name="character_list"),
    path(
        "character/<int:pk>/",
        views.CharacterDetailView.as_view(),
        name="character_detail",
    ),
    path("import-csv/", views.CSVImportView.as_view(), name="csv_import"),
]
