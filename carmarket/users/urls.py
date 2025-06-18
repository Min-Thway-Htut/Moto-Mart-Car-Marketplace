from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import home, search_car_brand_names
from django.conf import settings
from django.conf.urls.static import static
from listings import views as listings_views

urlpatterns = [
        path('', home, name='home'),
        path('signup/', views.signup, name='signup'),
        path('home/', views.home, name='home'),
        path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
        path('logout/', auth_views.LogoutView.as_view(), name="logout"),
        path('about/', views.about, name='about'),
        path('fandq/', views.fandq, name='fandq'),
        path('contact/', views.contact, name='contact'),
        path('car/<int:car_id>/edit/', views.edit_car, name='edit_car'),
        path('car/<int:car_id>/delete/', views.delete_car, name='delete_car'),
        path('search/', views.search_car_brand_names)
] 