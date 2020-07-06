from django.shortcuts import render
from django.http import HttpResponse
from .models import Product



# Create your views here.
def index(request):
    products =Product.objects.all()
    # return HttpResponse("<h1>Welcome to Django<h1>")
    return render(request,'index.html',{'products':products})
def about(request):
    return HttpResponse("<h1>About Page<h1>")
def contact(request):
    return HttpResponse("<h1>contact Page<h1> ")