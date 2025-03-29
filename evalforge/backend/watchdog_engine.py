import json
import logging
import subprocess
import threading
import time

logger = logging.getLogger(__name__)


def load_watchdog_config(config_path):
    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)


def monitor_services(config_path):
    config = load_watchdog_config(config_path)
    services = config.get("services", [])
    check_interval = config.get("check_interval", 10)

    while True:
        for svc in services:
            name = svc.get("name")
            check_cmd = svc.get("check_command")
            restart_cmd = svc.get("restart_command")
            try:
                result = subprocess.run(check_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                        timeout=5)
                if result.returncode != 0:
                    logger.warning(f"Service {name} is down. Restarting...")
                    subprocess.Popen(restart_cmd, shell=True)
            except Exception as e:
                logger.error(f"Error checking service {name}: {e}")
        time.sleep(check_interval)


def start_watchdog(config_path):
    thread = threading.Thread(target=monitor_services, args=(config_path,), daemon=True)
    thread.start()
