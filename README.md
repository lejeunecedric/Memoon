# Memoon — Content Structure Manager

> The creative backbone for your stories. From concept to screen, keep every element of your narrative organized.

## What is Memoon?

Memoon is a Django-powered content structure manager designed for creative teams and solo storytellers. Whether you're producing animated series, writing screenplays, or managing multimedia projects, Memoon helps you organize your content hierarchically — from the big picture down to the finest detail.

## Features

- **Hierarchical Organization**: Series → Seasons → Episodes → Sequences → Shots
- **Character & Wardrobe Management**: Track characters across seasons, manage their looks and costumes
- **Production-Ready Metadata**: Script, background descriptions, camera angles, movements, duration — all in one place
- **CSV Import**: Bulk import shots from CSV for rapid onboarding
- **Web Interface**: Beautiful, intuitive browsing of your entire content library
- **Admin Dashboard**: Full-featured Django admin for power users

## Quick Start

1. Activate the virtual environment:
```bash
cd /path/to/memoon
source venv/bin/activate
```

2. Run migrations (already done):
```bash
python manage.py migrate
```

3. Create a superuser:
```bash
python manage.py createsuperuser
```

4. Fire up the server:
```bash
python manage.py runserver 8089
```

5. Open your browser:
- **Web Interface**: http://127.0.0.1:8089/
- **Admin Panel**: http://127.0.0.1:8089/admin/

## Content Structure

Memoon organizes your project in a clear hierarchy:

| Level | Description |
|-------|-------------|
| **Series** | The complete work — title, description, overview |
| **Season** | A season/arc within the series |
| **Episode** | Individual episodes with titles and synopses |
| **Sequence** | Scenes within episodes — the building blocks |
| **Shot** | The atomic unit — camera angle, dialogue, characters, action |

### Supporting Elements

- **Characters**: Reusable across series, with detailed profiles
- **Wardrobe Items**: Every outfit, costume, or look for each character

## CSV Import

Got a spreadsheet full of shots? Import them in bulk:

```csv
sequence_number,sequence_title,shot_number,script,characters,wardrobe,background,camera_angle,camera_movement
1,Opening Scene,1,"Hero: Ready for this?","Hero","Suit","Downtown","Wide","Static"
1,Opening Scene,2,"Villain: You have no idea...","Villain","Cloak","Downtown","Close-up","Slow zoom"
2,The Chase,1,"[Action sequence]","Hero,Rival","Running Gear","Alleyway","Tracking","Follow"
```

## Why Memoon?

- **Structured, Not Rigid**: Define your own workflow within the hierarchy
- **Team-Ready**: Multiple users can work through the admin interface
- **Production-Proven**: Built for real creative workflows, not just demos
- **Open Source**: Extend and customize to your heart's content

## Tech Stack

- **Django 6.0.2** — The web framework
- **SQLite** — Zero-config database
- **Python 3.10+** — Core runtime

---

## 🚀 Deployment

### Option 1: UV (Recommended for Development)

```bash
# Install dependencies
make install

# Or with uv directly
uv sync

# Run the server
make run
```

### Option 2: Docker (Recommended for Production)

```bash
# Build and run
make docker

# Or manually:
docker build -t memoon:latest .
docker run -d -p 8089:8089 --name memoon memoon:latest
```

### Option 3: Manual

```bash
# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Start server
python manage.py runserver 8089
```

---

## 📋 Makefile Commands

| Command | Description |
|---------|-------------|
| `make install` | Install dependencies with uv |
| `make dev` | Install with dev dependencies |
| `make run` | Run development server |
| `make migrate` | Apply database migrations |
| `make createsuperuser` | Create admin user |
| `make test` | Run tests |
| `make clean` | Remove cache files |
| `make docker-build` | Build Docker image |
| `make docker-run` | Run Docker container |

---

*Memoon — because every great story deserves a great structure.*
