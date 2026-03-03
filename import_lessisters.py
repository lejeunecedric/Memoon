#!/usr/bin/env python
"""Import LesSisters PDF scripts into Memoon database."""

import os
import sys
import re
import django
import pdfplumber
from pathlib import Path

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cartoon_manager.settings")
sys.path.insert(0, "/home/c/Dev/Memoon")
django.setup()

from series.models import (
    Series,
    Season,
    Episode,
    Sequence,
    Shot,
    Character,
    ShotCharacter,
)


SCRIPTS_DIR = "/home/c/Dev/CartoonMem/LesSisters_scripts"

CHARACTER_ALIASES = {
    "COCORICO": "Coco",
    "DAILY": "Daily",
    "KRO": "Kro",
    "TIFF": "Tiff",
    "KILLIAN": "Killian",
    "WENDY": "Wendy",
    "AXEL": "Axel",
    "CHRISTELLE": "Christelle",
    "JULIE": "Julie",
    "TOM": "Tom",
    "MAMAN": "Maman",
    "PAPA": "Papa",
    "MEMERE": "Mémère",
    "NARRATEUR": "Narrateur",
}


def parse_filename_episode_info(filename):
    """Extract season and episode number from filename like LS5_23 or LS2_25."""
    match = re.search(r"LS(\d+)_(\d+)", filename)
    if match:
        season = int(match.group(1))
        episode = int(match.group(2))
        return season, episode

    match = re.search(r"LS_(\d+)_", filename)
    if match:
        num = int(match.group(1))
        if num > 30:
            return 1, num
        elif num > 20:
            return 2, num - 20
        elif num > 10:
            return 3, num - 10
        else:
            return 2, num

    return None, None


def extract_title_from_pdf(text):
    """Extract episode title from PDF text."""
    lines = text.split("\n")
    for line in lines[:10]:
        line = line.strip()
        if line and not line.startswith("LS") and len(line) > 3:
            if any(kw in line.upper() for kw in ["SCRIPT", "VBOARD", "VF", "VFINALE"]):
                continue
            return line
    return "Untitled Episode"


def parse_scenes_from_text(text):
    """Parse the PDF text into structured scenes."""
    scenes = []

    lines = text.split("\n")

    scene_pattern = re.compile(
        r"^\s*(\d+)\.\s*(INT\.|EXT\.)\s*(.+?)\s*[-–]\s*(JOUR|NUIT|AUBE|CREPUSCULE)?\.?\s*$",
        re.IGNORECASE,
    )
    scene_pattern2 = re.compile(
        r"^\s*(\d+)\.\s*(INT\.|EXT\.)\s*(.+?)\s*[-–]?\s*(JOUR|NUIT|AUBE|CREPUSCULE)?\.?\s*$",
        re.IGNORECASE,
    )
    scene_pattern3 = re.compile(
        r"^(INT\.|EXT\.)\s*(.+?)\s*[-–]\s*(JOUR|NUIT|AUBE|CREPUSCULE)?\.?\s*$",
        re.IGNORECASE,
    )
    dialogue_pattern = re.compile(
        r"^\s*(\d+)\.\s*([A-Z][A-Z0-9\s\-\']+)\s*(?:\(([^)]+)\))?\s*(.*)$"
    )

    current_scene = None
    current_dialogue = []
    scene_num_counter = 1

    for line in lines:
        line = line.strip()
        if not line:
            continue

        if "Cast List:" in line or line.isupper() and len(line) < 30:
            continue

        scene_match = scene_pattern.match(line)
        if not scene_match:
            scene_match = scene_pattern2.match(line)

        if scene_match:
            if current_scene:
                current_scene["dialogue"] = current_dialogue
                scenes.append(current_scene)

            scene_num = int(scene_match.group(1))
            setting = scene_match.group(3).strip() if scene_match.group(3) else ""
            time = scene_match.group(4) if scene_match.group(4) else ""

            current_scene = {
                "number": scene_num,
                "setting": setting,
                "time": time,
                "action": "",
                "dialogue": [],
            }
            current_dialogue = []
            continue

        scene_match3 = scene_pattern3.match(line)
        if scene_match3 and current_scene is None:
            setting = scene_match3.group(2).strip() if scene_match3.group(2) else ""
            time = scene_match3.group(3) if scene_match3.group(3) else ""
            current_scene = {
                "number": scene_num_counter,
                "setting": setting,
                "time": time,
                "action": "",
                "dialogue": [],
            }
            scene_num_counter += 1
            continue

        dialogue_match = dialogue_pattern.match(line)
        if dialogue_match and current_scene:
            char_name = dialogue_match.group(2).strip()
            mood = dialogue_match.group(3).strip() if dialogue_match.group(3) else ""
            dialogue_text = dialogue_match.group(4).strip()
            if dialogue_text:
                if mood:
                    current_dialogue.append(f"{char_name} ({mood}): {dialogue_text}")
                else:
                    current_dialogue.append(f"{char_name}: {dialogue_text}")
            continue

        if current_scene is not None:
            if current_dialogue:
                current_dialogue[-1] += " " + line
            else:
                current_scene["action"] += " " + line

    if current_scene:
        current_scene["dialogue"] = current_dialogue
        scenes.append(current_scene)

    if not scenes:
        all_scene_nums = []
        for pattern in [r"^(\d+)\.\s+(?:INT\.|EXT\.)", r"^(\d+)\s+(?:INT\.|EXT\.)"]:
            all_scene_nums.extend(re.findall(pattern, text, re.MULTILINE))
        for num in sorted(set(int(n) for n in all_scene_nums)):
            scenes.append(
                {"number": num, "setting": "", "time": "", "action": "", "dialogue": []}
            )

    return scenes


def extract_characters_from_scene(text):
    """Extract character names from dialogue in scene."""
    chars = set()
    for name in CHARACTER_ALIASES.keys():
        if name in text:
            chars.add(name)
    return list(chars)


def import_pdf_script(pdf_path):
    """Import a single PDF script into the database."""
    print(f"\n📄 Processing: {pdf_path.name}")

    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    if not text:
        print("  ⚠️ No text extracted from PDF")
        return None

    filename = pdf_path.name
    season_num, episode_num = parse_filename_episode_info(filename)

    if season_num is None:
        print(f"  ⚠️ Could not parse episode info from filename")
        season_num = 1
        episode_num = 1

    title = extract_title_from_pdf(text)
    print(f"  📺 Season {season_num}, Episode {episode_num}: {title}")

    series, _ = Series.objects.get_or_create(
        title="Les Sisters",
        defaults={"description": "Les Sisters - Animated French TV Series"},
    )

    season, _ = Season.objects.get_or_create(
        series=series, number=season_num, defaults={"title": f"Season {season_num}"}
    )

    episode, created = Episode.objects.get_or_create(
        season=season,
        number=episode_num,
        defaults={"title": title, "script": text[:5000], "script_status": "final"},
    )

    if not created:
        episode.script = text[:5000]
        episode.save()

    print(f"  ✅ Episode created/updated: {episode}")

    scenes = parse_scenes_from_text(text)
    print(f"  🎬 Found {len(scenes)} scenes (plans)")

    seq_num = 0
    current_seq = None

    for scene in scenes:
        if scene["number"] % 5 == 1:
            seq_num += 1
            current_seq, _ = Sequence.objects.get_or_create(
                episode=episode,
                number=seq_num,
                defaults={"title": f"Sequence {seq_num}"},
            )

        if current_seq is None:
            current_seq, _ = Sequence.objects.get_or_create(
                episode=episode, number=1, defaults={"title": "Sequence 1"}
            )

        script_content = scene.get("action", "")
        if scene.get("dialogue"):
            script_content += "\n\n" + "\n".join(scene["dialogue"])

        background = ""
        if scene.get("setting"):
            background = scene["setting"]
        if scene.get("time"):
            background += f" - {scene['time']}"

        shot, _ = Shot.objects.get_or_create(
            sequence=current_seq,
            number=scene["number"],
            defaults={
                "script": script_content[:2000],
                "background": background[:500],
                "notes": f"PLAN {scene['number']}",
            },
        )

        chars_in_scene = extract_characters_from_scene(script_content)
        for char_name in chars_in_scene:
            char_actual_name = CHARACTER_ALIASES.get(char_name, char_name)
            character, _ = Character.objects.get_or_create(
                name=char_actual_name,
                defaults={"description": f"Character from Les Sisters"},
            )
            character.series.add(series)

            ShotCharacter.objects.get_or_create(shot=shot, character=character)

    print(f"  ✅ Imported {len(scenes)} shots with characters")
    return episode


def main():
    """Main function to import all LesSisters PDFs."""
    print("🚀 Starting LesSisters import to Memoon...")
    print("=" * 50)

    scripts_dir = Path(SCRIPTS_DIR)
    if not scripts_dir.exists():
        print(f"❌ Directory not found: {scripts_dir}")
        return

    pdf_files = sorted(scripts_dir.glob("*.pdf"))

    if not pdf_files:
        print(f"❌ No PDF files found in {scripts_dir}")
        return

    print(f"Found {len(pdf_files)} PDF files to import")

    imported_count = 0
    for pdf_file in pdf_files:
        try:
            result = import_pdf_script(pdf_file)
            if result:
                imported_count += 1
        except Exception as e:
            print(f"  ❌ Error processing {pdf_file.name}: {e}")
            import traceback

            traceback.print_exc()

    print("\n" + "=" * 50)
    print(f"🎉 Import complete!")
    print(f"   Imported {imported_count} episodes")
    print(f"\nRun ./start.sh and visit http://localhost:8089/admin/")


if __name__ == "__main__":
    main()
