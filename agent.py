from google import genai
from config import API_KEY, MODEL_NAME
from google.genai.types import GenerateContentConfig


class TeluguAgent:
    def __init__(self, memory):
        self.memory = memory
        self.client = genai.Client(api_key=API_KEY)

    def think(self, user_text):
        prompt = f"""
You are a Telugu government assistant.

User said: "{user_text}"

Collected information so far:
{self.memory.get()}

Decide what to do next.

Respond ONLY in valid JSON:
{{
  "next_action": "ask" | "final",
  "question": "",
  "final_answer": ""
}}
"""

        response = self.client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
        config=GenerateContentConfig(
            tools=self.tools
))

        return response.text.strip()
