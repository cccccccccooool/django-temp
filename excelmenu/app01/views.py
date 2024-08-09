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
            print(category,items)
            elemt_dict[category] = items.split(',')
        print(elemt_dict)
    return JsonResponse(elemt_dict)