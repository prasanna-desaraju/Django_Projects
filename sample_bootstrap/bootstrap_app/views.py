from django.shortcuts import render, HttpResponse
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})
def add_product(request):
    product = Product(name = 'Mobile(lenovo)', description = 'Good' , price = '20000')
    product.save()
    return HttpResponse("Product record added successfully!")