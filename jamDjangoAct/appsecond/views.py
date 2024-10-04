from django.shortcuts import render

# Create your views here.
def contact(request):
    return render(request, 'appsecond/contact.html')

def blog(request):
    return render(request, 'appsecond/blog.html')

def productdetails(request):
    return render(request, 'appsecond/productdetails.html')