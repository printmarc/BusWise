"""To access keys: from config import key"""

from dotenv import load_dotenv
import os

load_dotenv()

TFL_API_KEY = os.getenv("TFL_API_KEY")
TOMTOM_API_KEY = os.getenv("TOMTOM_API_KEY")