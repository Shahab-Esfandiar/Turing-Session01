# app/use_cases/summarizer.py
import math
from core.logger import logger

class Summarizer:
    def __init__(self, llm_client):
        self.client = llm_client

    def summarize(self, text, prompt_template):
        """Generates summary and logs detailed metadata."""
        prompt = prompt_template.format(text_to_summarize=text)
        summary = self.client.predict(prompt)
        
        reading_time = self.estimate_reading_time(summary)
        
        # Log to file and terminal
        logger.info(f"[SUMMARIZER LOG] Input Words: {len(text.split())} | Output Words: {len(summary.split())} | Est. Reading Time: {reading_time}s")
        
        return summary, reading_time

    def estimate_reading_time(self, text: str) -> int:
        """Helper method: Establishes reading time (200 wpm)."""
        words = text.split()
        return math.ceil((len(words) / 200) * 60)