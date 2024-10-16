import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPEN_WEB_UI_API_KEY")
BASE_URL = os.getenv("OPEN_AI_API_BASE_URL")


class OpenWebUiApiClient:
    def __init__(self):
        self.base_url = BASE_URL
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}",
        }

    def get_completion(self, prompt, model="llama3.1:latest"):
        try:
            url = f"{self.base_url}/chat/completions"
            payload = {
                "model": model,
                "messages": [{"role": "user", "content": prompt}],
            }
            response = requests.post(
                url, json=payload, headers=self.headers, timeout=20
            )
            return response.json()["choices"][0]["message"]["content"]
        # .choices.message.content
        except Exception as e:  # Capture all exceptions
            # Log or print the error message
            print(f"An error occurred: {str(e)}")
            return None
