# System Health Check Script

## Description
This Python script is designed to perform a basic health check of your computer system. It verifies disk usage, CPU load, localhost IP address, and internet connectivity.

## Installation

**Prerequisites:**
- Python 3
- The `psutil` and `requests` libraries. If you don't have them installed, you can install them using pip:

```bash
pip install psutil requests
```
## Clone the repository or download the script file.
- Ensure you have the necessary permissions to execute the script.

# Usage
Run the script using Python 3 from your terminal:
```bash
./system_health_check.py
```

## Script Functions

### `check_disk_usage(disk)`
- Checks if the specified disk (e.g., `'/'` for the root disk on UNIX systems) has more than 20% free space.
- Returns `True` if the condition is met.

### `check_cpu_usage()`
- Checks if the CPU usage is below 75%.
- Returns `True` if the CPU usage is within acceptable limits.

### `check_localhost()`
- Verifies that the localhost IP address is correctly set to `'127.0.0.1'`.
- Returns `True` if localhost is correctly configured.

### `check_connectivity()`
- Attempts to connect to `https://www.google.com` to verify internet connectivity.
- Returns `True` if the connection is successful.

## Output
The script prints a status report indicating the operational status of each check:
- Disk Operational
- CPU Operational
- Localhost Operational
- Internet Operational

Each status is followed by `True` (operational) or `False` (not operational).
