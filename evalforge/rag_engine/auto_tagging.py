def auto_tag_summary(summary):
    # Very simple auto-tagging logic
    keywords = {
        "Speech": ["articulation", "phoneme", "speech"],
        "Language": ["comprehension", "expressive", "receptive"],
        "Fluency": ["stutter", "disfluency"],
        "Voice": ["hoarse", "nasal"]
    }
    for cat, keys in keywords.items():
        for key in keys:
            if key.lower() in summary.lower():
                return {"category": cat, "subcategory": key.capitalize()}
    return {"category": "General", "subcategory": "None"}
