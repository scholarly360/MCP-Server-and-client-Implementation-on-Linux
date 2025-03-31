# MCP-Server-and-client-Implementation-on-Linux
MCP Server and client Implementation on Linux (Rather than using Claude Desktop)

# MCP Server ::


## Create a new directory for our server 
uv init mcp_server_explore
cd mcp_server_explore

## Create virtual environment and activate it
uv venv
source .venv/bin/activate

## Install dependencies
uv add "mcp[cli]" 

## Create our server file
touch mcp_server_explore.py


# MCP Client ::


## Create a new directory for our client 
uv init mcp_client_explore
cd mcp_client_explore

## Create virtual environment and activate it
uv venv
source .venv/bin/activate

## Install dependencies
uv add mcp python-dotenv anthropic

## Create our server file
touch mcp_client_explore.py


# RUN  ::
uv run mcp_client_explore.py /workspaces/vsc_dev_mcp_explore/mcp_server_explore/mcp_server_explore.py 

# YouTube Video ::
https://youtu.be/53HvVkybgW8
