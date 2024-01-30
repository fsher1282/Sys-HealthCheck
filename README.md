# System Health Check Script

This script monitors various system health aspects, including disk usage, CPU usage, localhost connectivity, internet connectivity, and memory usage. It provides a flexible and configurable solution for ensuring that critical system resources are operating within acceptable thresholds.

## Features

- **Disk Usage Check**: Verifies that there's enough free space on the disk.
- **CPU Usage Check**: Checks if the CPU usage is below a set threshold.
- **Localhost Connectivity Check**: Ensures the localhost is correctly configured and reachable.
- **Internet Connectivity Check**: Tests the ability of the device to connect to the internet.
- **Memory Usage Check**: Monitors the percentage of used memory to ensure it's below the set threshold.
- **Configurable Thresholds**: Allows customization of thresholds for disk space, CPU, and memory usage.
- **Detailed Logging**: Utilizes Python's logging module to provide informative status reports and error messages.

## Prerequisites

- Python 3.x
- `psutil` library
- `requests` library

## Installation

Before running the script, ensure you have the required libraries installed. You can install them using pip:

```bash
pip install psutil requests
```

## Usage

1. **Modify the script parameters as needed:**
    - `DISK_USAGE_THRESHOLD`: The threshold for free disk space (percentage).
    - `CPU_USAGE_THRESHOLD`: The threshold for CPU usage (percentage).
    - `MEMORY_USAGE_THRESHOLD`: The threshold for memory usage (percentage).

2. **Run the script:**

    ```bash
    python system_health_check.py
    ```

3. **Check the logs for the status report.** If any checks fail, appropriate error messages will be logged.

## Contributing

Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.

