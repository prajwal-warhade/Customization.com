from django.shortcuts import render

# Create your views here.

def custom(request):
    return render(request,'login-registration.html')
