import uvicorn
import time
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Traditional REST Infrastructure API"
)

# ==================================================
# Request Models
# ==================================================

class DeviceUpdate(BaseModel):
    status: str
    temperature_c: float
    memory_usage_percent: int


class PartialDeviceUpdate(BaseModel):
    status: str = None


# ==================================================
# Simulated Database
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
# GET Device Status
# ==================================================

@app.get("/api/devices/{device_id}")
def get_device(device_id: str):

    print("📡 GET Device")
    time.sleep(2)

    if device_id not in DEVICES:
        raise HTTPException(404, "Device not found")

    return DEVICES[device_id]


# ==================================================
# GET Device Logs
# ==================================================

@app.get("/api/devices/{device_id}/logs")
def get_logs(device_id: str):

    print("📜 GET Logs")
    time.sleep(2)

    if device_id not in DEVICES:
        raise HTTPException(404, "Device not found")

    return {
        "logs": DEVICES[device_id]["logs"]
    }


# ==================================================
# POST Restart Device
# ==================================================

@app.post("/api/devices/{device_id}/restart")
def restart_device(device_id: str):

    print("🔄 POST Restart")
    time.sleep(2)

    if device_id not in DEVICES:
        raise HTTPException(404, "Device not found")

    DEVICES[device_id]["status"] = "online"
    DEVICES[device_id]["memory_usage_percent"] = 15

    return {
        "message": "Device restarted"
    }


# ==================================================
# PUT Full Update
# ==================================================

@app.put("/api/devices/{device_id}")
def update_device(
    device_id: str,
    payload: DeviceUpdate
):

    print("✏ PUT Update")
    time.sleep(2)

    if device_id not in DEVICES:
        raise HTTPException(404, "Device not found")

    DEVICES[device_id].update(
        payload.dict()
    )

    return {
        "message": "Device updated",
        "device": DEVICES[device_id]
    }


# ==================================================
# PATCH Partial Update
# ==================================================

@app.patch("/api/devices/{device_id}")
def patch_device(
    device_id: str,
    payload: PartialDeviceUpdate
):

    print("🛠 PATCH Update")
    time.sleep(2)

    if device_id not in DEVICES:
        raise HTTPException(404, "Device not found")

    if payload.status:
        DEVICES[device_id]["status"] = payload.status

    return {
        "message": "Device patched",
        "device": DEVICES[device_id]
    }


# ==================================================
# DELETE Device
# ==================================================

@app.delete("/api/devices/{device_id}")
def delete_device(device_id: str):

    print("🗑 DELETE Device")
    time.sleep(2)

    if device_id not in DEVICES:
        raise HTTPException(404, "Device not found")

    del DEVICES[device_id]

    return {
        "message": "Device deleted"
    }


# ==================================================
# Run Server
# ==================================================

if __name__ == "__main__":

    print("\n🚀 REST Server Running")
    print("🌐 Docs: http://127.0.0.1:8700/docs\n")

    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8700
    )