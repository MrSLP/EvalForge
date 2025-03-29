import psutil
import platform
import socket


def get_system_stats():
    return {
        "hostname": socket.gethostname(),
        "platform": platform.system(),
        "platform_version": platform.version(),
        "cpu": platform.processor(),
        "ram_gb": round(psutil.virtual_memory().total / (1024 ** 3), 2),
        "cpu_usage_percent": psutil.cpu_percent(interval=1),
        "ram_usage_percent": psutil.virtual_memory().percent
    }
