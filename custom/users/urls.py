from django.urls import path
from . import views

urlpatterns = [
             # Home page
    path('sign-in/', views.sign_in, name='sign_in'),  # Sign-in page
    path('sign_up/', views.sign_up, name='sign_up'),
    path('logout',views.user_logout),
    

]

