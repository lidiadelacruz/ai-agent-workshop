"""
Complete AI Agent - Tech News & Learning Assistant
This is the final, polished version ready for workshop demo.
"""

import google.generativeai as genai
from duckduckgo_search import DDGS
import json
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

# Configure the API
API_KEY = os.getenv("GEMINI_API_KEY")  # Replace with your key
genai.configure(api_key=API_KEY)


def web_search(query):
    """Search the web for current information"""
    print(f"\n🔍 Searching the web for: '{query}'")
    
    try:
        results = DDGS().text(query, max_results=5)
        
        search_results = []
        for i, result in enumerate(results, 1):
            search_results.append({
                "title": result.get("title", ""),
                "snippet": result.get("body", ""),
                "url": result.get("href", "")
            })
            print(f"   {i}. {result.get('title', 'N/A')}")
        
        # If no results, use mock data for demo
        if not search_results:
            print(f"   (Real search unavailable - using demo results)")
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
            for i, result in enumerate(search_results, 1):
                print(f"   {i}. {result['title']}")
        
        print(f"✓ Found {len(search_results)} results\n")
        return json.dumps(search_results, indent=2)
    
    except Exception as e:
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
            },
            {
                "title": "GitHub Copilot and AI Coding Assistants on the Rise",
                "snippet": "AI-powered coding tools are becoming essential for developers, with studies showing 30% improvement in coding speed.",
                "url": "https://example.com/tech-news-3"
            }
        ]
        for i, result in enumerate(mock_results, 1):
            print(f"   {i}. {result['title']}")
        print(f"✓ Found {len(mock_results)} results (demo mode)\n")
        return json.dumps(mock_results, indent=2)


# Define the tool for Gemini
web_search_tool = genai.protos.Tool(
    function_declarations=[
        genai.protos.FunctionDeclaration(
            name="web_search",
            description="Search the web for current information, news, tutorials, documentation, or any recent developments. Use this when you need up-to-date information.",
            parameters=genai.protos.Schema(
                type=genai.protos.Type.OBJECT,
                properties={
                    "query": genai.protos.Schema(
                        type=genai.protos.Type.STRING,
                        description="The search query"
                    )
                },
                required=["query"]
            )
        )
    ]
)


class TechAssistantAgent:
    """
    A Tech News & Learning Assistant that can:
    - Answer programming questions
    - Search for current tech news and tutorials
    - Remember conversation context
    """
    
    def __init__(self):
        self.model = genai.GenerativeModel(
            'gemini-2.5-flash',
            tools=[web_search_tool]
        )
        
        self.system_prompt = """You are a Tech News & Learning Assistant for computer science students.
        
        Your capabilities:
        - Answer programming and CS concept questions clearly
        - Search the web for current tech news, tutorials, and documentation
        - Provide code examples when helpful
        - Remember the conversation context
        
        Guidelines:
        - Be friendly and encouraging
        - Keep explanations clear and concise
        - Use web_search when you need current information or recent news
        - Provide practical, actionable advice
        """
        
        self.conversation_history = []
    
    def chat(self, user_message):
        """Send a message and get a response"""
        
        # Add user message
        self.conversation_history.append({
            "role": "user",
            "parts": [user_message]
        })
        
        # Start chat
        chat = self.model.start_chat(history=self.conversation_history[:-1])
        response = chat.send_message(user_message)
        
        # Agent loop - handle tool calls
        max_iterations = 5
        iteration = 0
        
        while iteration < max_iterations:
            iteration += 1
            
            # Check for tool calls
            if response.candidates[0].content.parts[0].function_call:
                function_call = response.candidates[0].content.parts[0].function_call
                
                if function_call.name == "web_search":
                    # Execute the search
                    query = function_call.args["query"]
                    search_results = web_search(query)
                    
                    # Send results back to model
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
                break
        
        # Get final response
        final_response = response.text
        
        # Add to history
        self.conversation_history.append({
            "role": "model",
            "parts": [final_response]
        })
        
        return final_response
    
    def clear_history(self):
        """Clear conversation history"""
        self.conversation_history = []
        print("✓ Conversation history cleared\n")


def interactive_demo():
    """Interactive demo - chat with the agent"""
    print("=" * 80)
    print("Tech News & Learning Assistant - Interactive Demo")
    print("=" * 80)
    print("\nCommands:")
    print("  - Type 'quit' or 'exit' to end")
    print("  - Type 'clear' to clear conversation history")
    print("  - Type 'help' to see example questions")
    print("\n" + "=" * 80 + "\n")
    
    agent = TechAssistantAgent()
    
    while True:
        user_input = input("You: ").strip()
        
        if not user_input:
            continue
        
        if user_input.lower() in ['quit', 'exit']:
            print("\nGoodbye! 👋\n")
            break
        
        if user_input.lower() == 'clear':
            agent.clear_history()
            continue
        
        if user_input.lower() == 'help':
            print("\nExample questions to try:")
            print("  - What is object-oriented programming?")
            print("  - What's new in Python 3.13?")
            print("  - How do I use Git branches?")
            print("  - What are the latest AI breakthroughs?")
            print("  - Explain recursion with an example")
            print()
            continue
        
        # Get response
        print()
        response = agent.chat(user_input)
        print(f"Agent: {response}\n")
        print("-" * 80 + "\n")


def scripted_demo():
    """Pre-scripted demo showing key features"""
    print("=" * 80)
    print("Tech News & Learning Assistant - Scripted Demo")
    print("=" * 80)
    print("\nThis demo shows:")
    print("1. Answering a programming question (no search)")
    print("2. Searching for current tech news (uses web search)")
    print("3. Using conversation memory (remembers context)")
    print("\n" + "=" * 80 + "\n")
    
    agent = TechAssistantAgent()
    
    # Demo 1: Programming question
    print("DEMO 1: Programming Question")
    print("-" * 40)
    question = "What is the difference between a list and a tuple in Python?"
    print(f"You: {question}\n")
    response = agent.chat(question)
    print(f"Agent: {response}\n")
    print("=" * 80 + "\n")
    
    # Demo 2: Current news (triggers web search)
    print("DEMO 2: Current Tech News")
    print("-" * 40)
    question = "What are the latest developments in large language models?"
    print(f"You: {question}\n")
    response = agent.chat(question)
    print(f"Agent: {response}\n")
    print("=" * 80 + "\n")
    
    # Demo 3: Memory
    print("DEMO 3: Conversation Memory")
    print("-" * 40)
    question = "Can you explain the first concept you mentioned in more detail?"
    print(f"You: {question}\n")
    response = agent.chat(question)
    print(f"Agent: {response}\n")
    print("=" * 80 + "\n")


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--interactive":
        interactive_demo()
    else:
        print("\nRunning scripted demo...")
        print("(Use 'python step5_complete_agent.py --interactive' for interactive mode)\n")
        scripted_demo()