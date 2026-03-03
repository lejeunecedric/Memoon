import opentimelineio as otio
from opentimelineio import opentime as opentime

from django.conf import settings


DEFAULT_FRAMERATE = 24


def duration_to_frames(duration):
    if duration is None:
        return DEFAULT_FRAMERATE * 3
    return int(duration.total_seconds() * DEFAULT_FRAMERATE)


def episode_to_timeline(episode, media_base_path=None, frame_rate=DEFAULT_FRAMERATE):
    media_path = media_base_path or getattr(settings, "OTIO_MEDIA_BASE_PATH", None)

    timeline = otio.schema.Timeline(name=str(episode), metadata={})

    video_track = otio.schema.Track(name="Video", kind=otio.schema.Track.Kind.Video)

    for sequence in episode.sequences.all().order_by("number"):
        track = otio.schema.Track(
            name=f"Seq{sequence.number}: {sequence.title or 'Sequence'}",
            kind=otio.schema.Track.Kind.Video,
        )

        for shot in sequence.shots.all().order_by("number"):
            duration_frames = duration_to_frames(shot.duration)
            source_range = otio.opentime.TimeRange(
                start_time=otio.opentime.RationalTime(0, frame_rate),
                duration=otio.opentime.RationalTime(duration_frames, frame_rate),
            )

            clip = otio.schema.Clip(
                name=f"Shot {shot.number}",
                source_range=source_range,
                metadata={
                    "shot_number": shot.number,
                    "script": shot.script or "",
                    "background": shot.background or "",
                    "camera_angle": shot.camera_angle or "",
                    "camera_movement": shot.camera_movement or "",
                    "notes": shot.notes or "",
                    "characters": [
                        {
                            "name": sc.character.name,
                            "wardrobe": sc.wardrobe.name if sc.wardrobe else None,
                            "notes": sc.notes or "",
                        }
                        for sc in shot.shotcharacter_set.select_related(
                            "character", "wardrobe"
                        ).all()
                    ],
                },
            )

            if media_path:
                media_url = f"{media_path}/shot_{shot.number}.mp4"
                clip.media_reference = otio.schema.ExternalReference(
                    target_url=media_url, available_range=source_range
                )

            track.append(clip)

        video_track.append(track)

    timeline.tracks.append(video_track)

    audio_track = otio.schema.Track(name="Audio", kind=otio.schema.Track.Kind.Audio)

    for sequence in episode.sequences.all().order_by("number"):
        for shot in sequence.shots.all().order_by("number"):
            duration_frames = duration_to_frames(shot.duration)
            source_range = otio.opentime.TimeRange(
                start_time=otio.opentime.RationalTime(0, frame_rate),
                duration=otio.opentime.RationalTime(duration_frames, frame_rate),
            )

            audio_clip = otio.schema.Clip(
                name=f"Shot {shot.number} Audio", source_range=source_range
            )

            if media_path:
                media_url = f"{media_path}/shot_{shot.number}.wav"
                audio_clip.media_reference = otio.schema.ExternalReference(
                    target_url=media_url, available_range=source_range
                )

            audio_track.append(audio_clip)

    timeline.tracks.append(audio_track)

    timeline.metadata["episode_title"] = episode.title
    timeline.metadata["episode_number"] = episode.number
    timeline.metadata["season_number"] = episode.season.number
    timeline.metadata["series_title"] = episode.season.series.title
    timeline.metadata["description"] = episode.description or ""

    return timeline


def export_episode(
    episode, format="otio", media_base_path=None, frame_rate=DEFAULT_FRAMERATE
):
    timeline = episode_to_timeline(episode, media_base_path, frame_rate)

    available = otio.adapters.available_adapter_names()
    if format == "fcpxml" and "fcp_xml" in available:
        return otio.adapters.write_to_string(timeline, adapter_name="fcp_xml")
    else:
        return otio.adapters.write_to_string(timeline, adapter_name="otio_json")
