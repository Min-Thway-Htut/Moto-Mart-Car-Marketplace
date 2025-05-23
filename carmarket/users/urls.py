from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import home

urlpatterns = [
        path('', home, name='home'),
        path('signup/', views.signup, name='signup'),
        path('home/', views.home, name='home'),
        path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
        path('logout/', auth_views.LogoutView.as_view(), name="logout"),
        path('about/', views.about, name='about'),
        path('fandq/', views.fandq, name='fandq'),
        path('contact/', views.contact, name='contact')
]