from langchain_core.tools import tool
from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv
import os

load_dotenv()

@tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@tool
def subtract(a: int, b: int) -> int:
    """Subtract two numbers"""
    return a - b

@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

@tool
def divide(a: int, b: int) -> float:
    """Divide two numbers"""
    return a / b

async def main():
    # Set up the model
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
    model = ChatGroq(model="llama3-8b-8192")
    
    # Create tools list
    tools = [add, subtract, multiply, divide]
    
    # Create the agent
    agent = create_react_agent(model, tools)

    # Test the agent
    response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "What is (2 + 2)*(3+3)?"}]}
    )
    print("Response:", response['messages'][-1].content)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
