# llm_endpoints.py

import sys

from google import genai
from pathlib import Path 

from app.core.utils import measure_latency


# -----------------------------
# Gemini Endpoint
# -----------------------------
@measure_latency
def gemini_ep(api_key: str, prompt: str, config, schema) -> str:
    """
    Generate response using Google Gemini.
    """
    print("Starting Gemini Client...")
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model=config['llm']['active_model'],
        contents=prompt,
        config={
            "response_mime_type": "application/json",
            "response_json_schema": schema.model_json_schema(),
            "temperature": config['llm']['temperature'],
            "top_p": config['llm']['top_p']
        },
    )

    return response.text


# -----------------------------
# GPT Endpoint
# -----------------------------
@measure_latency
def gpt_ep(api_key: str, prompt: str) -> str:
    """
    Generate response using OpenAI GPT.
    """
    pass


# -----------------------------
# Small Local Model Loader
# -----------------------------
def slm_load(model_name: str = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"):
    """
    Load a small local HuggingFace model.
    """
    pass

# -----------------------------
# Example Usage
# -----------------------------
if __name__ == "__main__":

    # domain exclusive implementation
    from config.config import CONFIG_PATH, read_config, GEMINI_API_KEY, SERP_API_KEY, FS_API_KEY, YELP_FUSION_API_KEY
    from app.core.schema import ExtractorOutput

    config = read_config(CONFIG_PATH)

    print(config)

    gemini_response = gemini_ep(
        GEMINI_API_KEY,
        "Generate a 3-day itinerary for a trip to Paris, including must-see attractions, dining recommendations, and local tips.",
        config,
        ExtractorOutput
    )

    print("Gemini Response:")
    print(gemini_response)
