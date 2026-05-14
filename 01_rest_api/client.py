import requests
import json
import time

SERVER = "http://127.0.0.1:8700"
DEVICE = "edge_node_1"


def show(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def run_demo():

    show("🤖 REST API DEMO")

    # GET
    print("\nSTEP 1: GET Device")

    response = requests.get(
        f"{SERVER}/api/devices/{DEVICE}"
    )

    print(
        json.dumps(
            response.json(),
            indent=2
        )
    )

    time.sleep(2)

    # GET LOGS
    print("\nSTEP 2: GET Logs")

    response = requests.get(
        f"{SERVER}/api/devices/{DEVICE}/logs"
    )

    print(
        json.dumps(
            response.json(),
            indent=2
        )
    )

    time.sleep(2)

    # POST
    print("\nSTEP 3: POST Restart")

    response = requests.post(
        f"{SERVER}/api/devices/{DEVICE}/restart"
    )

    print(
        json.dumps(
            response.json(),
            indent=2
        )
    )

    time.sleep(2)

    # PUT
    print("\nSTEP 4: PUT Update")

    payload = {
        "status": "maintenance",
        "temperature_c": 35,
        "memory_usage_percent": 20
    }

    response = requests.put(
        f"{SERVER}/api/devices/{DEVICE}",
        json=payload
    )

    print(
        json.dumps(
            response.json(),
            indent=2
        )
    )

    time.sleep(2)

    # PATCH
    print("\nSTEP 5: PATCH Device")

    response = requests.patch(
        f"{SERVER}/api/devices/{DEVICE}",
        json={
            "status": "offline"
        }
    )

    print(
        json.dumps(
            response.json(),
            indent=2
        )
    )

    time.sleep(2)

    # DELETE
    print("\nSTEP 6: DELETE Device")

    response = requests.delete(
        f"{SERVER}/api/devices/{DEVICE}"
    )

    print(
        json.dumps(
            response.json(),
            indent=2
        )
    )

    time.sleep(2)

    show("REST LIMITATIONS")

    print("❌ Must know all URLs")
    print("❌ Must know all HTTP verbs")
    print("❌ Must write glue code")
    print("❌ No tool discovery")

    print("\n✅ MCP solves all of this")


if __name__ == "__main__":
    run_demo()