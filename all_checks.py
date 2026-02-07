#!/usr/bin/env python3

import os
import sys
import psutil
import socket

def check_reboot():
    """Returns True if the computer has a pending reboot."""
    return os.path.exists("/run/reboot-required")

def check_cpu_usage(threshold=80):
    """Returns True if CPU usage is below threshold."""
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_usage}%")
    return cpu_usage < threshold

def check_memory_usage(threshold=80):
    """Returns True if memory usage is below threshold."""
    memory = psutil.virtual_memory()
    memory_percent = memory.percent
    print(f"Memory Usage: {memory_percent}%")
    return memory_percent < threshold

def check_disk_space(threshold=10, path="/"):
    """Returns True if disk space is above threshold (in GB)."""
    disk = psutil.disk_usage(path)
    disk_free_gb = disk.free / (1024**3)
    print(f"Disk Free Space: {disk_free_gb:.2f}GB")
    return disk_free_gb > threshold

def check_network_connectivity():
    """Returns True if internet connection is available."""
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        print("Network: Connected")
        return True
    except (socket.timeout, socket.error):
        print("Network: Disconnected")
        return False

def check_system_health():
    """Runs all health checks and returns overall status and failed checks."""
    print("=== Laptop Health Check ===\n")
    
    checks = {
        "Reboot Required": not check_reboot(),
        "CPU Usage": check_cpu_usage(),
        "Memory Usage": check_memory_usage(),
        "Disk Space": check_disk_space(),
        "Network": check_network_connectivity(),
        "Disk Full": full_disk()
    }
    
    print("\n=== Summary ===")
    failed_checks = []
    for check_name, status in checks.items():
        status_text = "✓ OK" if status else "✗ WARNING"
        print(f"{check_name}: {status_text}")
        if not status:
            failed_checks.append(check_name)
    
    return all(checks.values()), failed_checks

def main():
    all_passed, failed_checks = check_system_health()
    
    if not all_passed:
        print(f"\n⚠️  Failed Checks: {', '.join(failed_checks)}")
        sys.exit(1)
    print("\n✓ All health checks passed!")
    sys.exit(0)

main()
