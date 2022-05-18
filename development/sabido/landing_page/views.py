from django.shortcuts import render, redirect

# Create your views here.

def landing_page(request):
    return render(request, "landing_page/index.html")

