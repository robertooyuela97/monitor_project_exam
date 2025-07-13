from django.shortcuts import render
from monitor.system_info import get_cpu_usage, get_ram_usage, get_disk_usage, get_system_info

def home(request):
    context = {
        'cpu': get_cpu_usage(),
        'ram': get_ram_usage(),
        'disk': get_disk_usage(),
        'system': get_system_info()
    }
    return render(request, 'sistema/home.html', context)