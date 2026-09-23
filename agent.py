from dotenv import load_dotenv
from google import genai
import os

class Agent:
    def __init__(self):
        load_dotenv()

        self.client = genai.Client(
            api_key=os.getenv("GEMINI_API_KEY")
        )

        self.chat_session = self.client.chats.create(
            model="gemini-3.6-flash"
        )

    def chat(self, message):
        try:
            response = self.chat_session.send_message(message)

            return response.text

        except Exception as e:
            return f"Error: {e}"