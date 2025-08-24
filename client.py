from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_core.tools import tool
from langchain_groq import ChatGroq
from dotenv import load_dotenv

# from mcp_demo_langchain import weather
load_dotenv()
import asyncio
import os

async def main():
    client = MultiServerMCPClient(
        {
            "math": {"command": "python", "args": ["mathserver.py"], "transport": "stdio"},
            "weather":{"url":"http://localhost:8000/mcp/", "transport":"streamable_http"}
        }   
    )

    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

    tools = await client.get_tools()
    model = ChatGroq(model="llama3-8b-8192")
    agent = create_react_agent(model, tools)

    math_response = await agent.ainvoke(
            {"messages":[{"role": "user", "content": "What is 2 + 2?"}]}
    )
    print("Final response:", math_response['messages'][-1].content)
    # print("All messages:")
    # for i, msg in enumerate(math_response['messages']):
    #     print(f"Message {i}: {msg}")

    weather_response = await agent.ainvoke(
            {"messages": [{"role":"user", "content": "What is the weather of california"}]}
    )
    print("Final Response:", weather_response['messages'][-1].content)

asyncio.run(main())



