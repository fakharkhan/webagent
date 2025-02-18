import os
from typing import Optional, Type, Any
from dotenv import load_dotenv
from langchain_core.tools import BaseTool
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_react_agent
from langchain_community.utilities.serpapi import SerpAPIWrapper
from langchain_core.prompts import PromptTemplate

# Load environment variables
load_dotenv()

# Custom tool class with args schema
class SearchArgs(BaseModel):
    query: str = Field(description="search query to look up")

class CustomSerpAPITool(BaseTool):
    name: str = "web_search"
    description: str = "Search the web for current information"
    args_schema: Type[BaseModel] = SearchArgs
    
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self._search = SerpAPIWrapper()
        
    def _run(self, query: str) -> Any:
        """Use the tool."""
        return self._search.run(query)
        
    def _arun(self, query: str) -> Any:
        """Use the tool asynchronously."""
        raise NotImplementedError("CustomSerpAPITool does not support async")

def create_agent():
    # Validate API keys
    if not os.getenv("OPENAI_API_KEY"):
        raise ValueError("OPENAI_API_KEY environment variable is not set")
    if not os.getenv("SERPAPI_API_KEY"):
        raise ValueError("SERPAPI_API_KEY environment variable is not set")

    # Initialize the language model
    llm = ChatOpenAI(
        temperature=0,
        model="gpt-3.5-turbo"
    )

    # Initialize tools
    tools = [CustomSerpAPITool()]

    # Create the agent
    prompt = PromptTemplate.from_template(
        """Answer the following questions as best you can. You have access to the following tools:

        {tools}

        Use the following format:

        Question: the input question you must answer
        Thought: you should always think about what to do
        Action: the action to take, should be one of [{tool_names}]
        Action Input: the input to the action
        Observation: the result of the action
        ... (this Thought/Action/Action Input/Observation can repeat N times)
        Thought: I now know the final answer
        Final Answer: the final answer to the original input question

        Begin!

        Question: {input}
        {agent_scratchpad}"""
    )

    agent = create_react_agent(llm, tools, prompt)
    return AgentExecutor(agent=agent, tools=tools, verbose=True)

def main():
    try:
        # Create the agent
        agent = create_agent()
        
        # Example questions
        questions = [
            "What is the current weather in London?",
            "Who is the current president of France? What is their height in centimeters?"
        ]
        
        # Run the agent for each question
        for question in questions:
            try:
                print(f"\nQuestion: {question}")
                print("=" * 50)
                response = agent.invoke({"input": question})
                print(f"\nFinal Answer: {response['output']}\n")
            except Exception as e:
                print(f"Error processing question: {str(e)}")
                
    except ValueError as e:
        print(f"Configuration error: {str(e)}")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")

if __name__ == "__main__":
    main()
