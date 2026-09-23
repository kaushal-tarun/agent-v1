from dotenv import load_dotenv
from google import genai
import os

class Agent:
    def __init__(self):
        load_dotenv()

        self.client = genai.Client(
            api_key=os.getenv("GEMINI_API_KEY")
        )

    def chat(self, message):
        try:
            response = self.client.models.generate_content(
                model="gemini-3.6-flash",
                contents=message
            )

            return response.text

        except Exception as e:
            return f"Error: {e}"