"""
Check what models are available with your API key
"""

import google.generativeai as genai

# Configure the API
API_KEY = "AIzaSyD4yG6Q01d-mqtZClduQg0-kWpMtYyaLK4"  # Replace with your actual key
genai.configure(api_key=API_KEY)

print("Available models:\n")
for model in genai.list_models():
    if 'generateContent' in model.supported_generation_methods:
        print(f"- {model.name}")
        print(f"  Display name: {model.display_name}")
        print()