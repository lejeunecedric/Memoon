#!/bin/bash
# Memoon - Quick Start Script

set -e

echo "🚀 Starting Memoon..."

# Check if uv is available
if ! command -v uv &> /dev/null; then
    echo "📦 Installing uv..."
    pip install uv
fi

# Install dependencies if not already done
if [ ! -d ".venv" ]; then
    echo "📦 Creating virtual environment and installing dependencies..."
    uv venv .venv
    uv sync
fi

# Activate virtual environment
source .venv/bin/activate

# Run migrations
echo "🗄️ Running migrations..."
python manage.py migrate --noinput

# Start the server
echo "🌐 Starting server on http://localhost:8089"
python manage.py runserver 8089
