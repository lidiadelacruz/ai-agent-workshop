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

### 3. Clone This Repository
```bash
git clone https://github.com/YOUR_USERNAME/ai-agent-workshop.git
cd ai-agent-workshop
```

Or download and extract the ZIP file from GitHub.

### 4. Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 5. Install Dependencies
```bash
pip install -r requirements.txt
```

### 6. Get Gemini API Key
1. Go to [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Click "Create API Key"
3. Copy the key

### 7. Set Up Environment Variables
**Create a `.env` file in the project root:**

```bash
# On Mac/Linux
cp .env.example .env

# On Windows
copy .env.example .env
```

**Edit the `.env` file and add your API key:**

```
GEMINI_API_KEY=your_actual_api_key_here
```

**Important:** 
- Never commit your `.env` file to Git (it's already in `.gitignore`)
- The `.env` file keeps your API key secure and separate from your code

### 8. Test Your Setup
Run the test script:
```bash
python step1_setup.py
```

If you see a response from Gemini, you're ready! ✓

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
├── .env                     # Your API key (create this, never commit)
├── .env.example             # Example env file (committed to Git)
├── .gitignore              # Files to exclude from Git
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
pip install -r requirements.txt
```

Make sure your virtual environment is activated (you should see `(venv)` in your terminal).

### "API key not configured" or authentication errors
1. Check that your `.env` file exists in the project root
2. Verify the API key in `.env` is correct (no extra spaces or quotes)
3. Make sure you're running Python from the same directory as `.env`
4. Try printing the key to debug:
```python
import os
from dotenv import load_dotenv
load_dotenv()
print(f"API Key loaded: {os.getenv('GEMINI_API_KEY')[:10]}...")  # Shows first 10 chars
```

### "Model not found" error
Update the model name to `gemini-2.5-flash` or check available models:
```python
import google.generativeai as genai
for model in genai.list_models():
    if 'generateContent' in model.supported_generation_methods:
        print(model.name)
```

### Search not working
DuckDuckGo sometimes has rate limits or returns no results. The code includes mock fallback data for demos, so this shouldn't break your presentation.

### Virtual environment issues (Mac)
```bash
python3 -m venv venv
source venv/bin/activate
```

### `.env` file not loading
- Make sure it's named exactly `.env` (not `.env.txt`)
- It should be in the same directory where you run Python
- Check that `python-dotenv` is installed: `pip install python-dotenv`

## Security Best Practices

### Protecting Your API Key

**Never commit your API key to Git!** This workshop uses environment variables to keep your key secure.

✅ **DO:**
- Store your API key in `.env` file (already in `.gitignore`)
- Use `python-dotenv` to load the key
- Share `.env.example` as a template (without real keys)

❌ **DON'T:**
- Hardcode API keys directly in Python files
- Commit `.env` to Git
- Share your API key publicly or in screenshots

### What's Already Protected

This repository includes:
- `.gitignore` - Prevents `.env` from being committed
- `.env.example` - Shows students what to create without exposing your key
- Environment variable loading in all code files

### If You Accidentally Commit Your API Key

1. **Revoke it immediately** at [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Generate a new API key
3. Update your `.env` file
4. Use `git filter-branch` or BFG Repo-Cleaner to remove it from Git history

---

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

Happy coding! 🚀