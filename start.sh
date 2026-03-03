#!/bin/bash

# Start the Django development server on port 8089

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install dependencies if needed
if ! python -c "import django" 2>/dev/null; then
    echo "Installing Django..."
    pip install -r requirements.txt
fi

echo "Starting Django development server on port 8089..."
python manage.py runserver 8089
