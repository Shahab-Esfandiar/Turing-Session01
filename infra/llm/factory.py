# infra/llm/factory.py
from infra.llm.client import OpenAIClient
from infra.llm.ollama_client import OllamaClient
from core.exceptions import InvalidModelProvider
from core.logger import logger

class ClientFactory:
    @staticmethod
    def get_client(provider_name: str, specific_model=None):
        provider = provider_name.lower()
        # Changed to DEBUG so it won't show in terminal based on your request
        logger.debug(f"Initializing client for {provider_name} (Model: {specific_model})")
        
        if provider == "openai":
            return OpenAIClient(model_name=specific_model)
        elif provider == "ollama":
            return OllamaClient(model_name=specific_model) if specific_model else OllamaClient()
        else:
            raise InvalidModelProvider(f"Provider '{provider_name}' is not supported.")