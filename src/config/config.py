import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """
    Configuration class to manage application settings.
    """

    def __init__(self):
        self.GROQ_API_KEY = os.getenv("GROQ_API_KEY")

config = Config()