# Cartoon Series Manager

A Django application to manage cartoon series production, organizing content hierarchically from series down to individual shots.

## Features

- **Hierarchical Structure**: Series → Seasons → Episodes → Sequences → Shots
- **Shot Management**: Track script, characters, wardrobe, background, camera angle and movement
- **Character Management**: Manage characters and their wardrobe items
- **CSV Import**: Bulk import shots from CSV files
- **Admin Interface**: Full-featured Django admin for data management
- **Web Interface**: Browse series, seasons, episodes, sequences, shots, and characters

## Installation

1. Activate the virtual environment:
```bash
cd /tmp/cartoon_manager
source /tmp/cartoon_venv/bin/activate
```

2. Run migrations (already done):
```bash
python manage.py migrate
```

3. Create a superuser:
```bash
python manage.py createsuperuser
```

4. Run the development server:
```bash
python manage.py runserver
```

5. Open your browser:
- Web interface: http://127.0.0.1:8000/
- Admin interface: http://127.0.0.1:8000/admin/

## Data Structure

### Series
- Title, description
- Contains multiple seasons

### Season
- Season number
- Contains multiple episodes

### Episode
- Episode number and title
- Contains multiple sequences

### Sequence
- Sequence number and optional title
- Contains multiple shots

### Shot
- Shot number
- Script/dialogue
- Background description
- Camera angle
- Camera movement
- Duration
- Associated characters with wardrobe items

### Character
- Name and description
- Can appear in multiple series
- Has wardrobe items

### WardrobeItem
- Name and description
- Associated with a specific character

## CSV Import Format

Upload CSV files to bulk import shots. The CSV should have these columns:

- `sequence_number` (required): The sequence number
- `sequence_title` (optional): Title for the sequence
- `shot_number` (required): The shot number
- `script`: Dialogue/script text
- `characters`: Comma-separated character names
- `wardrobe`: Comma-separated wardrobe items (matches characters by position)
- `background`: Background description
- `camera_angle`: Camera angle description
- `camera_movement`: Camera movement description

### Example CSV:

```csv
sequence_number,sequence_title,shot_number,script,characters,wardrobe,background,camera_angle,camera_movement
1,Opening,1,"Hero: Let's go!","Hero","Cape","City Street","Wide shot","Static"
1,Opening,2,"Sidekick: Right behind you!","Hero,Sidekick","Cape,Casual","City Street","Medium shot","Pan right"
2,Chase,1,"Both running fast","Hero,Sidekick","Running Gear,Sportswear","Alleyway","Tracking shot","Follow movement"
```

## Usage

1. Start by creating a Series in the admin interface
2. Add Seasons and Episodes
3. Create Characters and their Wardrobe items
4. Add Sequences and Shots (via admin or CSV import)
5. Browse the web interface to view the hierarchy
6. Click through Series → Seasons → Episodes → Sequences → Shots to see details

## Navigation

- **Series List**: View all series
- **Characters**: View all characters
- **Import CSV**: Bulk import shots from CSV
- **Admin**: Full data management interface

## Development

The project uses:
- Django 6.0.2
- SQLite database
- Bootstrap-inspired styling (custom CSS)
