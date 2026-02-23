# infra/llm/client.py
from openai import OpenAI
import time
from core.config import settings
from core.exceptions import LLMServiceError
from core.logger import logger

class BaseLLMClient:
    """Abstract base class for all LLM clients."""
    def predict(self, prompt: str) -> str:
        raise NotImplementedError

class OpenAIClient(BaseLLMClient):
    def __init__(self, api_key=None, base_url=None, model_name=None):
        self.client = OpenAI(
            api_key=api_key or settings.API_KEY,
            base_url=base_url or settings.BASE_URL,
        )
        self.model_name = model_name or settings.MODEL_NAME

    def predict(self, prompt: str, retries=3, delay=2) -> str:
        """Send prompt to OpenAI with logging and retry logic."""
        logger.info(f"OpenAI Prediction started for model: {self.model_name}")
        for attempt in range(1, retries + 1):
            try:
                response = self.client.chat.completions.create(
                    model=self.model_name,
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.7
                )
                return response.choices[0].message.content.strip()
            except Exception as e:
                logger.error(f"OpenAI Attempt {attempt} failed: {e}")
                if attempt == retries:
                    raise LLMServiceError(f"OpenAI failed after {retries} retries.")
                time.sleep(delay)