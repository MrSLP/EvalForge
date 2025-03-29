import csv
import os
from datetime import datetime

TRACKER_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'eval_tracker.csv')


def save_approved_summary(filename, model, summary):
    is_new = not os.path.exists(TRACKER_FILE)
    with open(TRACKER_FILE, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        if is_new:
            writer.writerow(['timestamp', 'filename', 'model', 'summary'])
        writer.writerow([datetime.now().isoformat(), filename, model, summary])
