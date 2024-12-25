from django.shortcuts import render
from django.http import HttpResponse

from .models import Product

# Create your views here.
def displayList(request):
    prd1 = Product()
    prd1.name = 'Apple'
    prd1.price = '45'

    prd2 = Product()
    prd2.name = 'Banana'
    prd2.price = '67'

    products = []
    products.append(prd1)
    products.append(prd2)
    return render(request,'index.html',{'products': products})