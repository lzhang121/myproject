from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

def api_hello(request):
    return JsonResponse({'message': 'Hello, world!'})