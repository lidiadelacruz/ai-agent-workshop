"""
Step 1: Basic Setup - Getting Gemini API Working
This is our foundation. We'll connect to Google's Gemini API and make our first call.
"""

from google import genai

# Configure the API
# You'll need to get your API key from: https://aistudio.google.com/app/apikey
API_KEY = "AIzaSyD4yG6Q01d-mqtZClduQg0-kWpMtYyaLK4"  # Replace this with your actual API key

# Create a client instance
client = genai.Client(api_key=API_KEY)

# Make a simple API call
def test_connection():
    """Test if we can successfully call the Gemini API"""
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents="Hello! Can you introduce yourself in one sentence?"
    )
    print("Gemini says:", response.text)
    return response

if __name__ == "__main__":
    print("Testing Gemini API connection...")
    test_connection()
    print("\n✓ Success! API is working.")