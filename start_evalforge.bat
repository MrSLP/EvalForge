@echo off
call venv\Scripts\activate

echo Checking and installing required packages...
pip install -r requirements.txt

echo Starting Ollama...
start /B "" cmd /c "ollama run nous-hermes"
echo Waiting 10 seconds for Ollama to initialize...
timeout /t 10

echo Starting EvalForge Flask app...
call venv\Scripts\activate
set FLASK_APP=run.py
set FLASK_DEBUG=1
flask run --host=127.0.0.1 --port=5000
pause