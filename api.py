import os
from PIL import Image
import streamlit as st
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# Load secret tokens from local .env file
load_dotenv()

# Check local environment first, fallback to Streamlit Secrets for cloud deployment
HF_TOKEN = os.getenv("HF_TOKEN") or st.secrets.get("HF_TOKEN")

def generate_image(final_prompt: str) -> Image.Image:
    if not HF_TOKEN:
        raise ValueError("API Token missing! Please verify your .env file or Streamlit secrets config.")

    # Initialize the official Hugging Face inference manager
    client = InferenceClient(token=HF_TOKEN)

    # Use the client to contact the FLUX model directly
    image = client.text_to_image(
        prompt=final_prompt,
        model="black-forest-labs/FLUX.1-schnell"
    )
    
    return image