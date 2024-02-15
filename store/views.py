from django.shortcuts import render
from django.http import  HttpResponse, JsonResponse
from .models import *

# Create your views here.
def index(request):
    Products = Product.getall_prodcuts()
    return render(request, 'index.html', {'prodcuts' : Products })