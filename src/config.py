import dotenv
import os

dotenv.load_dotenv()

PICOVOICE_TOKEN = os.getenv('PICOVOICE_TOKEN')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')