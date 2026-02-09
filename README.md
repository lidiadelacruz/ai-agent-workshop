# AI Agent Workshop - Build a Tech Learning Assistant

A 90-minute hands-on workshop where you build an AI agent from scratch using Python and Google's Gemini API.

## What You'll Build

A **Tech News & Learning Assistant** that can:
- Answer programming questions
- Search the web for current tech news
- Remember conversation context
- Decide when to use tools autonomously

## Prerequisites

- Basic programming knowledge (variables, functions, loops)
- Python 3.8+ installed
- A code editor (VS Code recommended)
- Internet connection

## Setup (15 minutes)

### 1. Install Python
Check if you have Python:
```bash
python3 --version
```

If not installed, download from [python.org](https://www.python.org/downloads/)

### 2. Create Project Folder
```bash
mkdir ai-agent-workshop
cd ai-agent-workshop
```

### 3. Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 4. Install Dependencies
```bash
pip install google-generativeai duckduckgo-search
```

### 5. Get Gemini API Key
1. Go to [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Click "Create API Key"
3. Copy the key

### 6. Test Your Setup
Create `test.py`:
```python
import google.generativeai as genai

API_KEY = "YOUR_API_KEY_HERE"
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('gemini-2.5-flash')
response = model.generate_content("Say hello!")
print(response.text)
```

Run it:
```bash
python test.py
```

If you see a response, you're ready! ✓

## Workshop Steps

We'll build the agent in 4 progressive steps:

### Step 1: Setup & First API Call (10 min)
- Connect to Gemini API
- Make your first successful call
- **File:** `step1_setup.py`

### Step 2: Simple Agent (15 min)
- Create an Agent class
- Set up personality with system prompts
- Handle basic conversations
- **File:** `step2_simple_agent.py`

### Step 3: Add Memory (15 min)
- Implement conversation history
- Agent remembers context
- Multi-turn conversations
- **File:** `step3_agent_memory.py`

### Step 4: Add Tools (20 min)
- Implement web search tool
- Build the agent loop
- Agent decides when to search
- **File:** `step4_agent_tools.py`

### Step 5: Complete Agent (30 min)
- Polished final version
- Interactive mode
- Your turn to customize!
- **File:** `step5_complete_agent.py`

## Running the Examples

Each step builds on the previous one. Run them in order:

```bash
python step1_setup.py
python step2_simple_agent.py
python step3_agent_memory.py
python step4_agent_tools.py
python step5_complete_agent.py
```

For interactive chat with the final agent:
```bash
python step5_complete_agent.py --interactive
```

## Project Structure

```
ai-agent-workshop/
├── step1_setup.py           # Basic API connection
├── step2_simple_agent.py    # Simple chat agent
├── step3_agent_memory.py    # Agent with memory
├── step4_agent_tools.py     # Agent with web search
├── step5_complete_agent.py  # Complete polished agent
├── requirements.txt         # Dependencies
└── README.md               # This file
```

## Key Concepts

### What Makes It an "Agent"?

An AI agent has 4 key components:

1. **LLM (Brain)** - The language model that thinks
2. **Tools** - Functions the agent can call (like web search)
3. **Memory** - Conversation history for context
4. **Agent Loop** - The decision-making cycle:
   - Think: Should I use a tool?
   - Act: Call the tool
   - Observe: Get results
   - Respond: Use results to answer

### The Agent Loop

```python
while not done:
    response = model.chat(message)
    
    if response.wants_tool:
        result = execute_tool(response.tool_call)
        message = result  # Continue loop
    else:
        done = True  # Final answer
```

## Customization Ideas

After completing the workshop, try adding:

### New Tools
- **Code executor** - Run Python code snippets
- **Weather lookup** - Get current weather
- **Calculator** - Solve math problems
- **File reader** - Read and analyze files

### New Capabilities
- Save conversation history to file
- Add voice input/output
- Create a web interface
- Build a Discord/Slack bot
- Add multiple specialized tools

### Different Domains
- **Study Buddy** - Help with homework
- **Code Reviewer** - Find bugs in code
- **Research Assistant** - Summarize papers
- **Career Coach** - Job search help

## Resources

### Documentation
- [Gemini API Docs](https://ai.google.dev/docs)
- [Building AI Agents Guide](https://www.anthropic.com/research/building-effective-agents)

### Tutorials
- [Leonie Monigatti's AI Agent Tutorial](https://www.leoniemonigatti.com/blog/ai-agent-from-scratch-in-python.html)
- [FreeCodeCamp AI Agents Course](https://www.freecodecamp.org/news/build-an-ai-coding-agent-in-python/)

### Libraries & Frameworks
- **LangChain** - Framework for LLM applications
- **CrewAI** - Multi-agent systems
- **AutoGen** - Microsoft's agent framework

## Troubleshooting

### "Module not found" error
```bash
pip install google-generativeai duckduckgo-search
```

### "Model not found" error
Update the model name to `gemini-2.5-flash`

### Search not working
DuckDuckGo sometimes has rate limits. Try:
- Waiting a few seconds between searches
- Using more specific queries
- Checking your internet connection

### Virtual environment issues (Mac)
```bash
python3 -m venv venv
source venv/bin/activate
```

## Next Steps

1. **Complete the workshop** - Build all 5 steps
2. **Customize your agent** - Add new tools or change the domain
3. **Share your creation** - Show others what you built
4. **Learn frameworks** - Explore LangChain or CrewAI
5. **Build something real** - Create a tool you'll actually use

## Questions?

During the workshop, ask the instructor!

After the workshop:
- Check the [Gemini documentation](https://ai.google.dev/docs)
- Join coding communities on Discord/Reddit
- Review the resource links above

---

**Remember:** The goal isn't to memorize code, it's to understand how agents work so you can build your own!

