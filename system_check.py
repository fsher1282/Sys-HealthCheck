#!/usr/bin/env python3
import shutil
import psutil
import requests
import socket
import logging

# Configurable thresholds
DISK_USAGE_THRESHOLD = 20  # in percent
CPU_USAGE_THRESHOLD = 75   # in percent

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def check_disk_usage(disk, threshold=DISK_USAGE_THRESHOLD):
    # Verifies that there's enough free space on disk
    try:
        du = shutil.disk_usage(disk)
        free = du.free / du.total * 100
        return free > threshold, f"{free:.2f}% free space available"
    except FileNotFoundError:
        return False, "Disk not found"

def check_cpu_usage(threshold=CPU_USAGE_THRESHOLD):
    # Verifies that there's enough unused CPU
    try:
        usage = psutil.cpu_percent(1)
        return usage < threshold, f"CPU usage is {usage}%"
    except Exception as e:
        return False, str(e)

def check_localhost():
    # Checks if localhost is correctly configured
    try:
        localhost = socket.gethostbyname('localhost')
        return localhost == '127.0.0.1', f"localhost resolves to {localhost}"
    except socket.gaierror:
        return False, "Error resolving localhost"

def check_connectivity(url="https://www.google.com/", timeout=5):
    #Check if device can connect to internet
    try:
        response = requests.get(url, timeout=timeout)
        return response.status_code == 200, f"Internet connectivity to {url} successful"
    except requests.RequestException as e:
        return False, f"Internet connectivity failed: {str(e)}"

def check_memory_usage(threshold=75):
    #Check if there's enough free memory
    try:
        memory = psutil.virtual_memory()
        used = memory.used / memory.total * 100
        return used < threshold, f"Memory usage is {used}%"
    except Exception as e:
        return False, str(e)

def report_status():
    # Generates a status report of the system
    logging.info("Status Report...")

    checks = {
        "Disk Operational": check_disk_usage('/'),
        "CPU Operational": check_cpu_usage(),
        "Localhost Operational": check_localhost(),
        "Internet Operational": check_connectivity(),
        "Memory Usage": check_memory_usage()
    }

    for check, (status, message) in checks.items():
        if status:
            logging.info(f"{check}: OK - {message}")
        else:
            logging.error(f"{check}: FAILED - {message}")

if __name__ == "__main__":
    report_status()
