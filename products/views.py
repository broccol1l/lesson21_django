from django.shortcuts import render

from products.models import ProductModel
def home_page(request):
    products = ProductModel.objects.all()
    context = {'products': products}
    return render(request, "index.html", context=context)

def about_page(request):
    return render(request, "about.html")