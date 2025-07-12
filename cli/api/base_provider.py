from abc import ABC, abstractmethod

class BaseProvider(ABC):
    """
    Abstract base class for all language model providers.
    It ensures that every provider has a consistent interface.
    """

    @abstractmethod
    def get_response(self, prompt: str, config: dict) -> str:
        """
        Get a response from the language model.

        :param prompt: The input text to send to the model.
        :param config: A dictionary with provider-specific settings.
        :return: The response text from the model.
        """
        pass
