from django.shortcuts import render

def home (request):
    return render(request,'awwards/home.html')

def portfolio (request):
    return render(request,'awwards/portfolio.html')
