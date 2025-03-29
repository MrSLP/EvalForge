import requests
import socket
import time

HUB_URL = "http://127.0.0.1:5000/api/register_node"  # Change as needed

def register_node():
    data = {
        "hostname": socket.gethostname(),
        "ip": socket.gethostbyname(socket.gethostname()),
        "models": ["mistral", "llama2"],  # Example supported models
        "cpu": "N/A",  # Could add actual CPU info
        "ram": "N/A"   # Could add actual RAM info
    }
    try:
        response = requests.post(HUB_URL, json=data, timeout=10)
        print("Registration response:", response.json())
    except Exception as e:
        print("Failed to register node:", e)

if __name__ == "__main__":
    while True:
        register_node()
        time.sleep(30)  # Register every 30 seconds
