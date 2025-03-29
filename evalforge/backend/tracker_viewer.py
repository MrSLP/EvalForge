import csv
import os


def load_tracker():
    tracker_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'eval_tracker.csv')
    entries = []
    if os.path.exists(tracker_file):
        with open(tracker_file, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                entries.append(row)
    return entries
