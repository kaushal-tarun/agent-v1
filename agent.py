from dotenv import load_dotenv
from tools.calculator import calculator
from google import genai
import os

class Agent:
    def __init__(self):
        with open("prompts/system_prompt.txt", "r") as file:
            self.system_prompt = file.read()

        load_dotenv()

        self.client = genai.Client(
            api_key=os.getenv("GEMINI_API_KEY")
        )

        self.chat_session = self.client.chats.create(
            model="gemini-3.6-flash"
        )

    def chat(self, message):
        try:
            prompt = f"""
    {self.system_prompt}

    User: {message}
    """

            response = self.chat_session.send_message(prompt)

            return response.text

        except Exception as e:
            return f"Error: {e}"