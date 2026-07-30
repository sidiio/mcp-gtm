import os
from gtm_mcp.server import create_server

def main():
    port = int(os.environ.get("PORT", "8080"))
    mcp = create_server()
    mcp.run(transport="sse", host="0.0.0.0", port=port)

if __name__ == "__main__":
    main()
