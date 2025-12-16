"""Client for interacting with Gemini AI model using OpenAI-compatible API."""
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

GEMINI_OPENAPI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"


def create_ai_client():
    """
    Create and return an AI client for Gemini model.
    Returns:
        OpenAI: Configured AI client instance.
    """
    client = OpenAI(
        api_key=os.getenv("GEMINI_API_KEY"),
        base_url=GEMINI_OPENAPI_BASE_URL
    )

    print("AI client created successfully.")
    return client
