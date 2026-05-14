import time
from fastmcp import FastMCP

# ==================================================
# MCP Server
# ==================================================

mcp = FastMCP(
    name="⚡ Infrastructure Intelligence Server"
)

# ==================================================
# Simulated Device Database
# ==================================================

DEVICES = {
    "edge_node_1": {
        "status": "online",
        "temperature_c": 65.2,
        "memory_usage_percent": 88,
        "logs": [
            "[WARN] High memory usage",
            "[INFO] Application running"
        ]
    }
}


# ==================================================
# TOOLS
# ==================================================

@mcp.tool
def get_device(device_id: str):

    print("📡 Reading device...")
    time.sleep(2)

    return DEVICES.get(
        device_id,
        "Device not found"
    )


@mcp.tool
def get_logs(device_id: str):

    print("📜 Reading logs...")
    time.sleep(2)

    device = DEVICES.get(device_id)

    if not device:
        return "Device not found"

    return device["logs"]


@mcp.tool
def restart_device(device_id: str):

    print("🔄 Restarting device...")
    time.sleep(2)

    device = DEVICES.get(device_id)

    if not device:
        return "Device not found"

    device["status"] = "online"
    device["memory_usage_percent"] = 15

    return "Device restarted"


@mcp.tool
def update_device(
    device_id: str,
    status: str,
    temperature: float,
    memory: int
):

    print("✏ Updating device...")
    time.sleep(2)

    device = DEVICES.get(device_id)

    if not device:
        return "Device not found"

    device["status"] = status
    device["temperature_c"] = temperature
    device["memory_usage_percent"] = memory

    return device


@mcp.tool
def patch_device(
    device_id: str,
    status: str
):

    print("🛠 Patching device...")
    time.sleep(2)

    if device_id not in DEVICES:
        return "Device not found"

    DEVICES[device_id]["status"] = status

    return {
        "message": "Device patched successfully",
        "device": DEVICES[device_id]
    }


@mcp.tool
def delete_device(device_id: str):

    print("🗑 Deleting device...")
    time.sleep(2)

    if device_id not in DEVICES:
        return "Device not found"

    deleted = DEVICES.pop(device_id)

    return {
        "message": "Device deleted successfully",
        "deleted_device": deleted
    }


# ==================================================
# RESOURCE
# ==================================================

@mcp.resource("resource://system/info")
def system_info():

    return {
        "server": "Atlas-Core",
        "protocol": "MCP",
        "version": "1.0"
    }


# ==================================================
# RUN
# ==================================================

if __name__ == "__main__":

    print("\n🚀 MCP Server Running")
    print("🌐 http://localhost:8200")
    print("📡 /sse\n")

    mcp.run(
        transport="sse",
        port=8200
    )