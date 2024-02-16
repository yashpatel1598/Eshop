from django.shortcuts import render
from django.http import  HttpResponse, JsonResponse
from .models import *
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

# Create your views here.
def index(request):
    Products = Product.getall_prodcuts()
    Categorys = Category.getall_category()
    data = {}
    data['products'] = Products
    data['Categorys'] = Categorys
    return render(request, 'index.html', data)

class CategoryById(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, category_id):
        # print(category_id)

        if not category_id:
            Products = Product.getall_prodcuts()
            Categorys = Category.getall_category()
            data = {}
            data['products'] = Products
            data['Categorys'] = Categorys
            return render(request, 'index.html', data)
            
        cat_by_pro = Product.objects.filter(category = category_id)
        Categorys = Category.getall_category()
        # print(cat_by_pro)
        data = {}
        data['products'] = cat_by_pro
        data['Categorys'] = Categorys
        return render(request, 'index.html', data)

class SignUp(APIView):
    permission_classes = (AllowAny,)
    def get(self, request):
        return render(request,'signup.html')