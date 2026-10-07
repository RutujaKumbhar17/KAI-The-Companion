# config.py
import os

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# If using Groq, configure your Groq API Key and Model (e.g., 'llama-3.3-70b-versatile')
groq_api_key = os.environ.get("GROQ_API_KEY", "")
groq_model = os.environ.get("GROQ_MODEL", "llama-3.3-70b-versatile")

# Fallback OpenRouter / Gemini configuration (legacy)
apikey = os.environ.get("GEMINI_API_KEY", "")
model_name = os.environ.get("GEMINI_MODEL_NAME", "openai/gpt-3.5-turbo")

