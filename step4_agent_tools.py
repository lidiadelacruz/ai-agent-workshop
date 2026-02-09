"""
Step 4: Agent with Tools (Web Search)
Now the agent can use tools to search the web for current information.
"""

import google.generativeai as genai
from duckduckgo_search import DDGS
import json

# Configure the API
API_KEY = "AIzaSyD4yG6Q01d-mqtZClduQg0-kWpMtYyaLK4"  # Replace with your key
genai.configure(api_key=API_KEY)


# Define the web search tool
def web_search(query):
    """Search the web for current information"""
    print(f"🔍 Searching for: {query}")
    
    try:
        # Use DuckDuckGo to search
        results = DDGS().text(query, max_results=3)
        
        # Format the results
        search_results = []
        for result in results:
            search_results.append({
                "title": result.get("title", ""),
                "snippet": result.get("body", ""),
                "url": result.get("href", "")
            })
        
        # If no results, use mock data for demo
        if not search_results:
            print("   (Using demo results - real search unavailable)")
            search_results = [
                {
                    "title": "Latest AI Developments: Google DeepMind Announces Breakthrough",
                    "snippet": "Google DeepMind has announced significant advances in large language models, improving reasoning capabilities by 40% and reducing hallucinations through a new technique called 'grounded generation'.",
                    "url": "https://example.com/ai-news-1"
                },
                {
                    "title": "OpenAI Releases GPT-5 with Enhanced Multimodal Capabilities",
                    "snippet": "OpenAI's latest model shows remarkable improvements in code generation and mathematical reasoning. The model can now process video input in real-time and generate more accurate responses.",
                    "url": "https://example.com/ai-news-2"
                },
                {
                    "title": "New Study Shows AI Models Improving in Scientific Research",
                    "snippet": "Researchers demonstrate that modern LLMs can assist in drug discovery and materials science, cutting research time by up to 60% in initial hypothesis generation.",
                    "url": "https://example.com/ai-news-3"
                }
            ]
        
        return json.dumps(search_results, indent=2)
    except Exception as e:
        # Fallback to mock data on error
        print(f"   (Search error: {str(e)}, using demo results)")
        mock_results = [
            {
                "title": "Tech News: Latest Programming Trends",
                "snippet": "Python continues to dominate in data science and AI development. New frameworks are making AI development more accessible to developers.",
                "url": "https://example.com/tech-news-1"
            },
            {
                "title": "AI Research Breakthroughs in 2025",
                "snippet": "Major advancements in natural language processing and computer vision are transforming how we interact with technology.",
                "url": "https://example.com/tech-news-2"
            }
        ]
        return json.dumps(mock_results, indent=2)


# Define the tool schema for Gemini
web_search_tool = genai.protos.Tool(
    function_declarations=[
        genai.protos.FunctionDeclaration(
            name="web_search",
            description="Search the web for current information, news, tutorials, or documentation. Use this when you need up-to-date information that you don't have.",
            parameters=genai.protos.Schema(
                type=genai.protos.Type.OBJECT,
                properties={
                    "query": genai.protos.Schema(
                        type=genai.protos.Type.STRING,
                        description="The search query to look up"
                    )
                },
                required=["query"]
            )
        )
    ]
)


class AgentWithTools:
    """An AI agent that can use web search when needed"""
    
    def __init__(self):
        # Initialize the model with tools
        self.model = genai.GenerativeModel(
            'gemini-2.5-flash',
            tools=[web_search_tool]
        )
        
        # Set up the agent's personality/instructions
        self.system_prompt = """You are a helpful Tech News & Learning Assistant for computer science students.
        You help students with:
        - Answering programming questions
        - Explaining tech concepts
        - Finding current tech news and tutorials
        
        When you need current information or recent news, use the web_search tool.
        Be friendly, clear, and concise in your responses."""
        
        # Store conversation history
        self.conversation_history = []
    
    def chat(self, user_message):
        """Send a message to the agent and get a response"""
        
        # Add user message to history
        self.conversation_history.append({
            "role": "user",
            "parts": [user_message]
        })
        
        # Start chat with history
        chat = self.model.start_chat(history=self.conversation_history[:-1])
        
        # Get initial response
        response = chat.send_message(user_message)
        
        # Handle tool calls (this is the agent loop!)
        max_iterations = 5
        iteration = 0
        
        while iteration < max_iterations:
            iteration += 1
            
            # Check if the model wants to use a tool
            if response.candidates[0].content.parts[0].function_call:
                function_call = response.candidates[0].content.parts[0].function_call
                
                # Execute the tool
                if function_call.name == "web_search":
                    query = function_call.args["query"]
                    search_results = web_search(query)
                    
                    # Send the tool result back to the model
                    response = chat.send_message(
                        genai.protos.Content(
                            parts=[genai.protos.Part(
                                function_response=genai.protos.FunctionResponse(
                                    name="web_search",
                                    response={"result": search_results}
                                )
                            )]
                        )
                    )
                else:
                    break
            else:
                # No more tool calls, we have the final response
                break
        
        # Get the final text response
        final_response = response.text
        
        # Add assistant's response to history
        self.conversation_history.append({
            "role": "model",
            "parts": [final_response]
        })
        
        return final_response


def demo():
    """Demo the agent with web search"""
    print("=== Agent with Web Search Demo ===\n")
    
    # Create an agent
    agent = AgentWithTools()
    
    # Test 1: Question that doesn't need search
    print("You: What is a variable in programming?")
    response = agent.chat("What is a variable in programming?")
    print(f"Agent: {response}\n")
    print("-" * 80 + "\n")
    
    # Test 2: Question that DOES need search (current news)
    print("You: What are the latest developments in AI this week?")
    response = agent.chat("What are the latest developments in AI this week?")
    print(f"Agent: {response}\n")
    print("-" * 80 + "\n")
    
    # Test 3: Follow-up question (using memory)
    print("You: Can you give me more details about the first one?")
    response = agent.chat("Can you give me more details about the first one?")
    print(f"Agent: {response}\n")


if __name__ == "__main__":
    demo()