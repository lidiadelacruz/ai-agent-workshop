"""
Step 2: Simple Agent - Basic Chat
Now we build an Agent class that can have conversations.
"""

import google.generativeai as genai

# Configure the API
API_KEY = "AIzaSyD4yG6Q01d-mqtZClduQg0-kWpMtYyaLK4"  # Replace with your key
genai.configure(api_key=API_KEY)


class SimpleAgent:
    """A basic AI agent that can respond to messages"""
    
    def __init__(self):
        # Initialize the model
        self.model = genai.GenerativeModel('gemini-2.5-flash')
        
        # Set up the agent's personality/instructions
        self.system_prompt = """You are a helpful Tech News & Learning Assistant for computer science students.
        You help students with:
        - Answering programming questions
        - Explaining tech concepts
        - Finding current tech news and tutorials
        
        Be friendly, clear, and concise in your responses."""
    
    def chat(self, user_message):
        """Send a message to the agent and get a response"""
        
        # Combine system prompt with user message
        full_prompt = f"{self.system_prompt}\n\nUser: {user_message}\nAssistant:"
        
        # Get response from Gemini
        response = self.model.generate_content(full_prompt)
        
        return response.text


def demo():
    """Demo the simple agent"""
    print("=== Simple Agent Demo ===\n")
    
    # Create an agent
    agent = SimpleAgent()
    
    # Have a conversation
    questions = [
        "What is Python used for?",
        "Can you explain what a variable is?",
        "What's the difference between Java and Python?"
    ]
    
    for question in questions:
        print(f"You: {question}")
        response = agent.chat(question)
        print(f"Agent: {response}\n")


if __name__ == "__main__":
    demo()