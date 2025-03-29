class SmartPromptBuilder:
    def __init__(self, memory_store_instance):
        self.memory = memory_store_instance

    def build_prompt(self, new_text, category="Speech", num_examples=3):
        # Retrieve the last approved summaries in the same category
        examples = [entry["summary"] for entry in self.memory.memory
                    if entry["approved"] and entry["category"].lower() == category.lower()]
        examples = examples[-num_examples:] if len(examples) >= num_examples else examples
        prompt = "Based on the following examples, generate a summary in the same style:\n"
        for ex in examples:
            prompt += f"Example: {ex}\n"
        prompt += f"\nNow summarize the following evaluation:\n{new_text}"
        return prompt
