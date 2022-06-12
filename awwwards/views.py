from django.shortcuts import render



def register(request):
    return render(request,'awwards/register.html')


def login(request):
    return render(request,'awwards/login.html')


def home (request):
    
    return render(request,'awwards/home.html')

def portfolio (request):
    
    return render(request,'awwards/portfolio.html')
