# Web Search AI Agent

This project implements an AI agent using LangChain that can answer questions by searching the web using SerpAPI.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up API keys:

For Unix/Linux/macOS:
```bash
export OPENAI_API_KEY='your-openai-api-key'
export SERPAPI_API_KEY='your-serpapi-api-key'
```

For Windows (Command Prompt):
```cmd
set OPENAI_API_KEY=your-openai-api-key
set SERPAPI_API_KEY=your-serpapi-api-key
```

For Windows (PowerShell):
```powershell
$env:OPENAI_API_KEY='your-openai-api-key'
$env:SERPAPI_API_KEY='your-serpapi-api-key'
```

Alternatively, copy `.env.template` to `.env` and fill in your API keys.

3. Run the agent:
```bash
python web_agent.py
```

## Features

- Uses latest versions of langchain packages
- Implements custom SerpAPI tool with proper args schema
- Shows agent's thought process in verbose mode
- Example questions included
