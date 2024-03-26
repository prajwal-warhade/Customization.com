from django.shortcuts import render

# Create your views here.

def custom(request):
    return render(request,'index.html')
