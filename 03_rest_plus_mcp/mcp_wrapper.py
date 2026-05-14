import time
import requests
from fastmcp import FastMCP

# ==================================================
# MCP Wrapper Server
# ==================================================

mcp = FastMCP(
    name="⚡ REST API Wrapper Server"
)

# Base URL for the existing REST API
REST_BASE_URL = "http://127.0.0.1:8700/api"

# ==================================================
# TOOLS
# ==================================================

@mcp.tool
def get_device(device_id: str):
    print("📡 Calling REST GET /devices/{device_id}...")
    response = requests.get(f"{REST_BASE_URL}/devices/{device_id}")
    if response.status_code == 200:
        return response.json()
    return f"Error: {response.status_code} - {response.text}"


@mcp.tool
def get_logs(device_id: str):
    print("📜 Calling REST GET /devices/{device_id}/logs...")
    response = requests.get(f"{REST_BASE_URL}/devices/{device_id}/logs")
    if response.status_code == 200:
        return response.json()
    return f"Error: {response.status_code} - {response.text}"


@mcp.tool
def restart_device(device_id: str):
    print("🔄 Calling REST POST /devices/{device_id}/restart...")
    response = requests.post(f"{REST_BASE_URL}/devices/{device_id}/restart")
    if response.status_code == 200:
        return response.json()
    return f"Error: {response.status_code} - {response.text}"


@mcp.tool
def update_device(
    device_id: str,
    status: str,
    temperature: float,
    memory: int
):
    print("✏ Calling REST PUT /devices/{device_id}...")
    payload = {
        "status": status,
        "temperature_c": temperature,
        "memory_usage_percent": memory
    }
    response = requests.put(f"{REST_BASE_URL}/devices/{device_id}", json=payload)
    if response.status_code == 200:
        return response.json()
    return f"Error: {response.status_code} - {response.text}"


@mcp.tool
def patch_device(
    device_id: str,
    status: str
):
    print("🛠 Calling REST PATCH /devices/{device_id}...")
    payload = {
        "status": status
    }
    response = requests.patch(f"{REST_BASE_URL}/devices/{device_id}", json=payload)
    if response.status_code == 200:
        return response.json()
    return f"Error: {response.status_code} - {response.text}"


@mcp.tool
def delete_device(device_id: str):
    print("🗑 Calling REST DELETE /devices/{device_id}...")
    response = requests.delete(f"{REST_BASE_URL}/devices/{device_id}")
    if response.status_code == 200:
        return response.json()
    return f"Error: {response.status_code} - {response.text}"


# ==================================================
# RESOURCE
# ==================================================

@mcp.resource("resource://system/info")
def system_info():
    return {
        "server": "REST-Wrapper",
        "protocol": "MCP",
        "version": "1.0",
        "backend": REST_BASE_URL
    }


# ==================================================
# RUN
# ==================================================

if __name__ == "__main__":
    print("\n🚀 MCP Wrapper Server Running")
    print("🌐 http://localhost:8300")
    print("📡 /sse\n")
    print(f"🔗 Forwarding requests to {REST_BASE_URL}")

    mcp.run(
        transport="sse",
        port=8300
    )
