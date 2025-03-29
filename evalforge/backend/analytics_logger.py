import json
import os
from datetime import datetime

LOG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'usage_log.json')


def log_event(event_type, data):
    entry = {
        "timestamp": datetime.now().isoformat(),
        "event": event_type,
        "data": data
    }
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")
