# Google Tag Manager (GTM) MCP Server

Google Tag Manager MCP server with OAuth authentication. Connects Claude.ai and other MCP clients directly to your GTM containers and tags via Google login — no server-side OAuth credentials required.

Built with Python [FastMCP](https://github.com/jlowin/fastmcp) using `RemoteAuthProvider`, following the same zero-credential architecture as the GA4 and Google Search Console MCP servers.

## How it works

The server uses FastMCP's `RemoteAuthProvider` which advertises Google as the authorization server. When you click **Connect** in Claude.ai, Claude handles the Google OAuth flow itself and passes the bearer token to the server. The server validates the token via Google's `tokeninfo` endpoint — no Google client secrets or keys needed on the server side.

## Tools

- **`list_accounts`** — Lists all GTM accounts you have access to
- **`list_containers`** — Lists all containers within a specific GTM account
- **`list_workspaces`** — Lists active workspaces in a container
- **`list_tags`** — Displays all configured tags in a workspace
- **`list_triggers`** — Displays all triggers (pageviews, clicks, custom events) in a workspace
- **`list_variables`** — Lists all user-defined and built-in variables

## Deployment on Coolify

### 1. Connect Repository in Coolify

Point Coolify at this public repository (`https://github.com/sidiio/mcp-gtm`). 
Set **Build Pack** to `Dockerfile`.

### 2. Set Environment Variables

In your application environment settings, add:

| Variable | Value |
|---|---|
| `PORT` | `8080` |
| `MCP_BASE_URL` | `https://mcpgtm.tophathome.ca` |

*No Google client secrets or OAuth keys required in Coolify.*

### 3. Connect in Claude.ai

1. Open **Claude.ai → Settings → Connectors (Integrations)**
2. Click **Add custom integration**
3. URL: `https://mcpgtm.tophathome.ca`
4. Click **Connect** → Google login pop-up appears → sign in with your account → done!

## Local Development

```bash
pip install -e .
MCP_BASE_URL=http://localhost:8080 python -m gtm_mcp
