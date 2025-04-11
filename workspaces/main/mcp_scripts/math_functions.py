import os
import math
from mcp.server.fastmcp import FastMCP
import json

port = int(os.getenv("MCP_PORT"))
mcp = FastMCP("SimpleServer", port=port, host="0.0.0.0")


@mcp.tool()
def add(a: float, b: float) -> float:
    """
    Returns the sum of two integers.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The sum of a and b.
    """
    print(f"Adding two numbers - a: {a}, b: {b}")

    return a + b

@mcp.tool()
def multiply(a: float, b: float) -> float:
    """
    Returns the product of two integers.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The product of a and b.
    """
    print(f"Multiplying two numbers - a: {a}, b: {b}")

    return a * b

@mcp.tool()
def ln(a: float) -> float:
    """
    Returns the natural logarithm of a number.

    Args:
        a (float): The number.

    Returns:
        float: The natural logarithm of a.
    """
    print(f"Calculating natural logarithm - a: {a}")
    
    return math.log(a)


symbols = {
    "pi": "π",
    "plus": "+",
    "minus": "-",
    "multiply": "×",
    "divide": "÷",
    "equals": "=",
    "greater_than": ">",
    "less_than": "<",
    "square_root": "√",
    "infinity": "∞",
    "integral": "∫",
    "summation": "Σ",
    "factorial": "!",
    "degree": "°",
    "percent": "%"
}

@mcp.resource("resource://math_symbols", mime_type="application/json", name="List of available math symbols")
def get_symbols() -> str:
    """
    Retrieves a list of all symbol keys.

    Returns:
        list[str]: A list containing the keys of the symbols dictionary.
    """

    print("Retrieving all symbol keys")

    result = {
        'symbols' : list(symbols.keys())
    }

    return json.dumps(result)

@mcp.resource("resource://math_symbols/{symbol_name}", name="Get a math symbol by its name")
def get_symbol(symbol_name: str) -> str:
    """
    Returns the symbol for a given symbol name.

    Args:
        symbol_name (str): The name of the symbol.

    Returns:
        str: The symbol.
    """
    print(f"Retrieving symbol for {symbol_name}")

    return symbols.get(symbol_name)


mcp.run(transport = "sse")