from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather Server")

@mcp.tool()
def get_weather(city: str) -> str:
    """_summary_
    Get the weather for a city
    """
    return "The weather in " + city + " is sunny"

if __name__ == "__main__":
    mcp.run(transport="streamable-http")