# app/use_cases/translator.py
from core.logger import logger

class Translator:
    def __init__(self, llm_client):
        self.client = llm_client

    def translate(self, text, source, target, tone, prompt_template):
        """Translates text and logs character-based metrics."""
        prompt = prompt_template.format(
            text=text,
            source=source,
            target=target,
            tone=tone
        )
        translation = self.client.predict(prompt)
        
        logger.info(f"[TRANSLATOR LOG] Tone: {tone} | Original Chars: {len(text)} | Translated Chars: {len(translation)}")
        return translation