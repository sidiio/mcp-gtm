"""Google OAuth 2.1 authentication layer using FastMCP's built-in GoogleProvider."""

import os
from fastmcp.server.auth import GoogleProvider

GTM_SCOPE = "https://www.googleapis.com/auth/tagmanager.readonly"

def create_auth_provider(base_url: str) -> GoogleProvider:
    """Creates a GoogleProvider OAuthProxy configured for Google Tag Manager."""
    client_id = os.environ.get("GOOGLE_CLIENT_ID", "")
    client_secret = os.environ.get("GOOGLE_CLIENT_SECRET", "")

    return GoogleProvider(
        client_id=client_id,
        client_secret=client_secret,
        base_url=base_url,
        scopes=[GTM_SCOPE],
    )
