import json
import os
from datetime import datetime

RESTORE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'restore_points')
os.makedirs(RESTORE_DIR, exist_ok=True)


def create_restore_point(state_data, name=""):
    timestamp = datetime.now().isoformat().replace(":", "-")
    filename = f"restore_{name}_{timestamp}.json" if name else f"restore_{timestamp}.json"
    filepath = os.path.join(RESTORE_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(state_data, f, indent=2)
    return filepath


def list_restore_points():
    return [f for f in os.listdir(RESTORE_DIR) if f.endswith('.json')]


def load_restore_point(filename):
    filepath = os.path.join(RESTORE_DIR, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


def delete_restore_point(filename):
    filepath = os.path.join(RESTORE_DIR, filename)
    os.remove(filepath)
