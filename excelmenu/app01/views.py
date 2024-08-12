from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'menu.html')

def getElemt(request):
    elemt_dict = {}
    with open('./app01/static/txt/elemt.txt', "r", encoding='utf-8') as fp:
        lines = fp.read()
        lines = lines.split('@')
        for line in lines:
            category, items = line.strip().split(':')
            elemt_dict[category] = items.split(',')
    return JsonResponse(elemt_dict)

def print_ip(request):
    ip_data={}
    with open('./app01/static/txt/ip.txt', "r", encoding='utf-8') as fp:
        lines = fp.read()
        lines=lines.split('\n')
        for i,line in enumerate(lines):
            ip_data[i]=line
    return JsonResponse(ip_data)
