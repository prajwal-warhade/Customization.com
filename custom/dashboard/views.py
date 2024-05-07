from django.shortcuts import render
from users.models import UserProfile
from product.models import Product 
# Create your views here.

def index(request):
    if request.user.is_authenticated:
        user_profile = UserProfile.objects.filter(user=request.user).first()
        products = Product.objects.filter(is_active=True)
        context = {
            'prod': products,
            'data1': user_profile
        }
    else:
        products = Product.objects.filter(is_active=True)
        context = {'prod': products}
        
    return render(request, 'index.html', context)

def profile(request):
    user_profile = UserProfile.objects.filter(user=request.user)
    context = {
        'data': user_profile,
        'data1': user_profile
    }
    return render(request, 'profile.html', context)