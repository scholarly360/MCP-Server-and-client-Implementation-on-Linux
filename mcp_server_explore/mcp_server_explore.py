"""
Yogi :: Two simple tools listed here 
"""
from typing import Any
import sys
from mcp.server.fastmcp import FastMCP
# Initialize FastMCP server
mcp = FastMCP("Explore the MCP")
print("Server env is :: ", sys.prefix)

@mcp.tool()
async def add_numbers(value1: int, value2:int) -> int:
    """Add Two numbers

    Args:
        value1: First Integer value
        value2: Second Integer value

    Returns:
        int: Addition of two numbers
    """
    return value1 + value2

@mcp.tool()
async def multiply_numbers(value1: int, value2:int) -> int:
    """Multiply Two numbers

    Args:
        value1: First Integer value
        value2: Second Integer value


    Returns:
        int: Multiplication of two numbers
    """
    
    return value1 * value2

if __name__ == "__main__":
    # Initialize and run the server
    print("Server env is ", sys.prefix)
    mcp.run(transport='stdio')

# uv run mcp_server_explore.py
