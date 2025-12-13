import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
GOOGLE_APPLICATION_CREDENTIALS = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
DRIVE_FOLDER_ID = os.getenv('DRIVE_FOLDER_ID')


GEMINI_MODEL = "gemini-flash-latest"  

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file")
if not GOOGLE_APPLICATION_CREDENTIALS:
    raise ValueError("GOOGLE_APPLICATION_CREDENTIALS not found in .env file")
if not DRIVE_FOLDER_ID:
    raise ValueError("DRIVE_FOLDER_ID not found in .env file")

print("✅ Configuration loaded successfully!")