"""
Step 3: Agent with Memory
Now the agent can remember previous messages in the conversation.
"""

import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

# Configure the API
API_KEY = os.getenv("GEMINI_API_KEY")  # Replace with your key
genai.configure(api_key=API_KEY)


class AgentWithMemory:
    """An AI agent that remembers the conversation"""
    
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
        
        # THIS IS NEW: Store conversation history
        self.conversation_history = []
    
    def chat(self, user_message):
        """Send a message to the agent and get a response"""
        
        # Add user message to history
        self.conversation_history.append({
            "role": "user",
            "parts": [user_message]
        })
        
        # Create a chat session with the full history
        chat = self.model.start_chat(history=self.conversation_history[:-1])
        
        # Get response
        response = chat.send_message(user_message)
        
        # Add assistant's response to history
        self.conversation_history.append({
            "role": "model",
            "parts": [response.text]
        })
        
        return response.text


def demo():
    """Demo the agent with memory"""
    print("=== Agent with Memory Demo ===\n")
    
    # Create an agent
    agent = AgentWithMemory()
    
    # Have a multi-turn conversation
    print("You: What is Python?")
    response = agent.chat("What is Python?")
    print(f"Agent: {response}\n")
    
    print("You: What did I just ask you?")
    response = agent.chat("What did I just ask you?")
    print(f"Agent: {response}\n")
    
    print("You: Can you give me a code example?")
    response = agent.chat("Can you give me a code example?")
    print(f"Agent: {response}\n")


if __name__ == "__main__":
    demo()