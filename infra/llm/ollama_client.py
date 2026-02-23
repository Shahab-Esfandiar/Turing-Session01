# infra/llm/ollama_client.py
import ollama
import time
from infra.llm.client import BaseLLMClient
from core.exceptions import LLMServiceError
from core.logger import logger

class OllamaClient(BaseLLMClient):
    def __init__(self, model_name="gemma3:4b", system_prompt="You are a helpful assistant."):
        self.model_name = model_name
        self.system_prompt = system_prompt
        self.messages = [{"role": "system", "content": self.system_prompt}]

    def predict(self, prompt: str, retries=3, delay=2) -> str:
        logger.info(f"Ollama Prediction started using model: {self.model_name}")
        self.messages.append({"role": "user", "content": prompt})
        for attempt in range(1, retries + 1):
            try:
                response = ollama.chat(model=self.model_name, messages=self.messages)
                answer = response['message']['content']
                self.messages.append({"role": "assistant", "content": answer})
                return answer
            except Exception as e:
                logger.error(f"Ollama Attempt {attempt} failed: {e}")
                if attempt == retries:
                    raise LLMServiceError(f"Ollama failed after {retries} retries.")
                time.sleep(delay)