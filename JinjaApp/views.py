from django.shortcuts import render

# Create your views here.

def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def home(request):
    return render(request, 'base.html')
def home2(request):
    return render(request, 'home.html')