from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'appone/home.html')

def product(request):
    return render(request, 'appone/product.html')

def about(request):
    return render(request, 'appone/about.html')