import psutil
import platform
import os

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_ram_usage():
    mem = psutil.virtual_memory()
    return {
        'total_gb': round(mem.total / (1024**3), 2),
        'used_gb': round(mem.used / (1024**3), 2),
        'percent': mem.percent
    }

def get_disk_usage():
    disk = psutil.disk_usage('/')
    return {
        'total_gb': round(disk.total / (1024**3), 2),
        'used_gb': round(disk.used / (1024**3), 2),
        'free_gb': round(disk.free / (1024**3), 2),
        'percent': disk.percent
    }

def get_system_info():
    return {
        'os': platform.system(),
        'release': platform.release(),
        'version': platform.version(),
        'cpu_cores': os.cpu_count()
    }