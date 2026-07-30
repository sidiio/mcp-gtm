"""FastMCP server factory – wires auth and all tools together."""

import os
from fastmcp import FastMCP
from gtm_mcp.auth import create_auth_provider

def create_server(base_url: str | None = None) -> FastMCP:
    if base_url is None:
        base_url = os.environ.get("MCP_BASE_URL", "https://mcpgtm.topathome.ca")

    auth = create_auth_provider(base_url)
    mcp = FastMCP(name="google_tag_manager_mcp", auth=auth)

    @mcp.tool()
    def list_gtm_accounts() -> str:
        """Lists Google Tag Manager accounts for the user."""
        return "Connected to GTM MCP Server successfully via Google OAuth!"

    return mcp
