import os
from openai import OpenAI
from config import OPENAI_API_KEY

class OpenAIClient:
    def __init__(self):
        self.client = OpenAI(
            api_key=OPENAI_API_KEY,
        )
    
    def get_response(self, user_input):
        try:
            response = self.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_input}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {str(e)}"