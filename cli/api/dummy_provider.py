from .base_provider import BaseProvider

class DummyProvider(BaseProvider):
    """
    A dummy provider that echoes the prompt.
    Useful for testing the application without making real API calls.
    """

    def get_response(self, prompt: str, config: dict) -> str:
        """
        Returns the prompt prefixed with 'Echo: '.
        """
        return f"Echo: {prompt}"
