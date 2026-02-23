# core/exceptions.py
class AIAppError(Exception):
    """Base class for all application-specific exceptions."""
    pass

class LLMServiceError(AIAppError):
    """Raised when an external LLM service (OpenAI/Ollama) fails."""
    pass

class PromptTemplateError(AIAppError):
    """Raised when a prompt file is missing or template formatting fails."""
    pass

class EmptyInputError(AIAppError):
    """Raised when the user provides empty text for processing."""
    pass

class InvalidModelProvider(AIAppError):
    """Raised when an unsupported model provider is requested."""
    pass