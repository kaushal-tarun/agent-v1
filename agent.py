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
        response = self.client.models.generate_content(
            model="gemini-3.8-flash",
            contents=message
        )

        return response.text