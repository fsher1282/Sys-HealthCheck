#!/usr/bin/env python3
import shutil
import psutil
import requests
import socket


def check_disk_usage(disk):
    # Verifies that there's enough free space on disk
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20


def check_cpu_usage():
    # Verifies that there's enough unused CPU
    usage = psutil.cpu_percent(1)
    return usage < 75


def check_localhost():
    localhost = socket.gethostbyname('localhost')
    if localhost == '127.0.0.1':
        return True
    else:
        return False


def check_connectivity():
    # Check if device can connect to internet
    request = requests.get('https://www.google.com/')
    if str(request) == '<Response [200]>':
        return True
    else:
        return False


if __name__ == "__main__":
    disk_status = check_disk_usage('/')
    cpu_status = check_cpu_usage()
    local_status = check_localhost()
    internet_status = check_connectivity()

    print("Status Report...")
    print('Disk Operational:' + str(disk_status))
    print('CPU Operational:' + str(cpu_status))
    print('Localhost Operational: ' + str(local_status))
    print('Internet Operational: ' + str(internet_status))
