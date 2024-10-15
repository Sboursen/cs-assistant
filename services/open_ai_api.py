from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('OPEN_AI_API_KEY')


class OpenAiApiClient:
    def __init__(self):
        self.client = OpenAI(api_key=API_KEY)

    def get_completion(self, prompt, model="gpt-4o-mini"):
        try:
            messages = [{"role": "user", "content": prompt}]
            response = self.client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=0
            )
            return response.choices[0].message.content
        except Exception as e:  # Capture all exceptions
            # Log or print the error message
            print(f"An error occurred: {str(e)}")
            return None
