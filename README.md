# Web Search AI Agent

An intelligent agent built with LangChain that can answer questions by searching the web using SerpAPI and processing results with OpenAI's GPT model.

## Requirements

- Python 3.9+
- OpenAI API key
- SerpAPI key

## Installation

1. Clone the repository and create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

Set up your API keys using one of these methods:

### Method 1: Environment Variables

For Unix/Linux/macOS:
```bash
export OPENAI_API_KEY='your-openai-api-key'
export SERPAPI_API_KEY='your-serpapi-api-key'
```

For Windows (PowerShell):
```powershell
$env:OPENAI_API_KEY='your-openai-api-key'
$env:SERPAPI_API_KEY='your-serpapi-api-key'
```

### Method 2: .env File

Create a .env file in the project root:
```
OPENAI_API_KEY=your-openai-api-key
SERPAPI_API_KEY=your-serpapi-api-key
```

## Usage

Run the agent:
```bash
python web_agent.py
```

The agent will process two example questions:
- Current weather in London
- Information about the French president

Example output:
```
Question: What is the current weather in London?
==================================================
Thought: I need to search for current weather information in London
Action: web_search
Action Input: current weather London
Observation: [Search results...]
Final Answer: [Weather details...]

Question: Who is the current president of France? What is their height in centimeters?
==================================================
...
```

## Features

- 🔍 Web search capabilities using SerpAPI
- 🤖 OpenAI GPT-3.5 Turbo integration
- 📝 Detailed thought process logging
- ⚡ Efficient error handling
- 🛠️ Custom tool implementation
- 🔒 Secure API key management

## Troubleshooting

- Ensure both API keys are properly set
- Check internet connectivity for web searches
- Verify Python version compatibility
- Make sure all dependencies are correctly installed

## Dependencies

Key packages:
- langchain and related packages
- openai
- python-dotenv
- google-search-results (SerpAPI)

For full list, see `requirements.txt`
