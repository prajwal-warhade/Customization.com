from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from users.models import UserProfile

def sign_in(request):
    if request.method == 'GET':
        return render(request, 'login-register/login-registration.html')
    else:
        username = request.POST['user_email']
        password = request.POST['user_password']
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect("/index/")
        else:
            # Handle invalid credentials
            return render(request, 'login-register/login-registration.html', {'errmsg': 'Invalid credentials'})

def sign_up(request):
    if request.method == 'GET':
        return render(request, 'login-register/login-registration.html')
    elif request.method == 'POST':
        name = request.POST['name']
        username = request.POST['uname']
        password = request.POST['upass']
        confirm_password = request.POST['ucpass']
        
        if name == '' or username == '' or password == '' or confirm_password == '':
            return render(request, 'login-register/login-registration.html', {'errmsg': 'Fields cannot be blank'})
        elif password != confirm_password:
            return render(request, 'login-register/login-registration.html', {'errmsg': 'Password and Confirm Password do not match'})
        elif len(password) < 8:
            return render(request, 'login-register/login-registration.html', {'errmsg': 'Password must be at least 8 characters'})
        else:
            try:
                user = User.objects.create_user(username=username, password=password)
                UserProfile.objects.create(user=user, name=name, email=username)
                return render(request, 'login-register/login-registration.html', {'success': 'Successfully registered'})
            except Exception:
                return render(request, 'login-register/login-registration.html', {'errmsg': 'User already exists or an error occurred'})

def user_logout(request):
    logout(request)
    return redirect('sign_up')

#index function is on dashboard.views
     
#profile function is on dashboard.views