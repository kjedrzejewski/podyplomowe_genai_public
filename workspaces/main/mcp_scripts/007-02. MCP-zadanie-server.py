import os
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Directory operator")

dir_path = "007-02. MCP-working_dir"

@mcp.tool()
def echo(msg: str) -> str:
    """
    Echoes the input message.

    Args:
        msg (str): The message to echo.
    """
    return f"Otrzymano wiadomość: {msg}"

# Miejsce na Wasze narzędzia





mcp.run(transport = "stdio")