@echo off
cd /d "%~dp0"
where python >nul 2>&1 || (echo Python not found. Install from python.org & pause & exit /b 1)
if not exist .venv python -m venv .venv
call .venv\Scripts\activate.bat
pip install -r requirements.txt || (echo Install failed & pause & exit /b 1)
echo Open http://127.0.0.1:5000
python app.py
pause
