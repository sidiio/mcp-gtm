import os
import uvicorn
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP Server
mcp = FastMCP("mcp-gtm", host="0.0.0.0", port=8080)

@mcp.tool()
def list_gtm_accounts() -> str:
    """Lists Google Tag Manager accounts for the configured service account."""
    # Place actual Google Tag Manager API call logic here
    return "GTM MCP Server connected successfully! Service account active."

def main():
    print("Starting GTM MCP Server on port 8080...")
    # Run the MCP server with SSE transport
    mcp.run(transport="sse")

if __name__ == "__main__":
    main()
