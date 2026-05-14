import asyncio
import json
from mcp import ClientSession
from mcp.client.sse import sse_client


def show_rpc(method, params):
    rpc_request = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params
    }
    print("\n📤 JSON-RPC Request to Wrapper:")
    print(json.dumps(rpc_request, indent=2))


def show_response(result):
    print("\n📥 JSON-RPC Response from Wrapper:")
    print(json.dumps(result, indent=2))


async def run_agent():
    print("\n" + "=" * 70)
    print("🤖 MCP AGENT (REST WRAPPER DEMO)")
    print("=" * 70)

    try:
        # Connecting to the wrapper port 8300
        async with sse_client("http://localhost:8300/sse") as (read, write):
            async with ClientSession(read, write) as session:

                print("\n🔌 Connecting to Wrapper...")
                await session.initialize()
                await asyncio.sleep(2)

                # Tool discovery
                print("\n🔍 Discovering tools...")
                tools = await session.list_tools()

                for tool in tools.tools:
                    print(f"⚙ {tool.name}")

                await asyncio.sleep(2)

                # ---------------------------------
                # GET DEVICE
                # ---------------------------------

                show_rpc(
                    "tools/call",
                    {
                        "name": "get_device",
                        "arguments": {
                            "device_id": "edge_node_1"
                        }
                    }
                )

                result = await session.call_tool(
                    "get_device",
                    arguments={
                        "device_id": "edge_node_1"
                    }
                )

                for item in result.content:
                    try:
                        show_response(json.loads(item.text))
                    except (json.JSONDecodeError, TypeError):
                        show_response({"text": item.text})

                await asyncio.sleep(2)

                # ---------------------------------
                # GET LOGS
                # ---------------------------------

                show_rpc(
                    "tools/call",
                    {
                        "name": "get_logs",
                        "arguments": {
                            "device_id": "edge_node_1"
                        }
                    }
                )

                result = await session.call_tool(
                    "get_logs",
                    arguments={
                        "device_id": "edge_node_1"
                    }
                )

                for item in result.content:
                    try:
                        show_response(json.loads(item.text))
                    except (json.JSONDecodeError, TypeError):
                        show_response({"text": item.text})

                await asyncio.sleep(2)

                # ---------------------------------
                # PATCH
                # ---------------------------------

                show_rpc(
                    "tools/call",
                    {
                        "name": "patch_device",
                        "arguments": {
                            "device_id": "edge_node_1",
                            "status": "offline"
                        }
                    }
                )

                result = await session.call_tool(
                    "patch_device",
                    arguments={
                        "device_id": "edge_node_1",
                        "status": "offline"
                    }
                )

                for item in result.content:
                    try:
                        show_response(json.loads(item.text))
                    except (json.JSONDecodeError, TypeError):
                        show_response({"text": item.text})

                await asyncio.sleep(2)

                print("\n✅ Hybrid flow complete")

    except Exception as e:
        print(f"\n❌ Error: {e}")


if __name__ == "__main__":
    asyncio.run(run_agent())
