@echo off
echo Starting Memoon development server...
echo.
cd /d "%~dp0"
python manage.py runserver
pause
