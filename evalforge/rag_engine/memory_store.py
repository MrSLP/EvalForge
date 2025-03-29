import json
import os
from datetime import datetime

MEMORY_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'summaries.json')


def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_memory(data):
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


class SummaryMemoryStore:
    def __init__(self):
        self.memory = load_memory()

    def add_summary(self, summary, category, subcategory, approved=True):
        entry = {
            "timestamp": datetime.now().isoformat(),
            "summary": summary,
            "category": category,
            "subcategory": subcategory,
            "approved": approved
        }
        self.memory.append(entry)
        save_memory(self.memory)

    def reject_summary(self, summary):
        # Mark entries with matching summary as rejected
        for entry in self.memory:
            if entry["summary"] == summary:
                entry["approved"] = False
        save_memory(self.memory)

    def search(self, query):
        # A simple keyword search in summaries
        results = []
        for entry in self.memory:
            if query.lower() in entry["summary"].lower():
                results.append(entry)
        return results
