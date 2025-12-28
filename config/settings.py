import os
from dotenv import load_dotenv


class Settings:
    """
    Settings class is responsible for loading and providing
    environment configuration securely.
    """

    def __init__(self):
        load_dotenv()

    def load_api_key(self) -> str:
        """
        Load Gemini API key from environment variables.

        Returns:
            str: Gemini API key

        Raises:
            ValueError: If API key is not found
        """
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY not found. Please set it in the .env file."
            )

        return api_key
