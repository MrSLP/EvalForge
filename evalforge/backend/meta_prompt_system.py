import json
import os
from datetime import datetime

FEEDBACK_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'prompt_feedback.json')


def save_feedback(prompt, feedback):
    entry = {
        "timestamp": datetime.now().isoformat(),
        "prompt": prompt,
        "feedback": feedback
    }
    try:
        data = []
        if os.path.exists(FEEDBACK_FILE):
            with open(FEEDBACK_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
        data.append(entry)
        with open(FEEDBACK_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        print(f"Error saving feedback: {e}")


def get_feedback():
    if os.path.exists(FEEDBACK_FILE):
        with open(FEEDBACK_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []
