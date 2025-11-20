from django.shortcuts import render
from django.http import HttpResponse

from configapp.models import Product, Supplier


# Create your views here.
def index(request):
    product = Product.objects.all()
    supplier = Supplier.objects.all()
    context = {
        'product': product,
        'title': 'Products',
        'supplier': supplier,
    }
    return render(request,'index.html',context)
