# core/config.py
import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    def __init__(self):
        self.API_KEY = os.getenv("API_KEY")
        self.BASE_URL = os.getenv("BASE_URL")
        self.MODEL_NAME = os.getenv("MODEL_NAME", "gpt-3.5-turbo")

        if not self.API_KEY:
            print("[Warning] API_KEY not found. Ensure it's set if using OpenAI.")

settings = Settings()