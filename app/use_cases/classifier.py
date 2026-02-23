# app/use_cases/classifier.py
from core.logger import logger

class TextClassifier:
    def __init__(self, llm_client):
        self.client = llm_client

    def classify(self, text, prompt_template):
        """Classifies text and logs the model response."""
        prompt = prompt_template.format(text=text)
        response = self.client.predict(prompt)
        
        logger.info(f"[CLASSIFIER LOG] Model Response: {response}")
        return response