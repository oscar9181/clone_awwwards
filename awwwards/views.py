
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm



def register(request):
    form=UserCreationForm
    context ={'form':form}
    return render(request,'awwards/register.html',context)


def login(request):
    form=UserCreationForm
    context ={'form':form}
    return render(request,'awwards/login.html',context)


def home (request):
    
    return render(request,'awwards/home.html')

def portfolio (request):
    
    return render(request,'awwards/portfolio.html')
