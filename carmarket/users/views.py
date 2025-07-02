from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponseForbidden
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from listings.forms import CarForm
from listings.models import Car, SearchQuery
import random
import traceback
from django.db import IntegrityError
import logging
from .models import CarBrandNames
from faker import Faker
from .forms import CustomUserCreationForm

fake = Faker()



def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/signup.html', {'form': form})


@login_required
def home(request):
    query = request.GET.get('search', '')
    sort_order = request.GET.get('sort', '')

    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            car = form.save(commit=False)
            car.owner = request.user
            car.save()
            return redirect('home')
    else:
        form = CarForm()

    cars = Car.objects.all()

    if query:
        search_obj, created = SearchQuery.objects.get_or_create(term=query)
        if not created:
            search_obj.count += 1
            search_obj.save()
        cars = cars.filter(title__icontains=query)

    if sort_order == 'price_asc':
        cars = cars.order_by('price')
    elif sort_order == 'price_desc':
        cars = cars.order_by('-price')

    paginator = Paginator(cars, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    top_searches = SearchQuery.objects.order_by('-count')[:5]
    return render(request, 'users/home.html', 
                  {'form': form, 
                   'page_obj': page_obj,
                   'top_searches': top_searches})

@login_required
def about(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            car = form.save(commit=False)
            car.owner = request.user
            car.save()
    else:
        form = CarForm()

    user_cars = Car.objects.filter(owner=request.user)
    return render(request, 'users/about.html', {'form': form, 'cars': user_cars})

def edit_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if car.owner != request.user:
        return redirect('home')
    
    car.title = request.POST.get('title')
    car.description = request.POST.get('description')
    car.price = request.POST.get('price')
    car.year = request.POST.get('year')

    if request.FILES.get('image'):
        car.image = request.FILES.get('image')

    car.save()
    return redirect('home')

def delete_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if request.method == 'POST':
        car.delete()
        return redirect('home')
    return render(request, 'users/delete_car.html', {'car': car})


def fandq(request):
    faqs = [
        {"question": "How do I list my car for sale?", "answer": "You can list your car by creating an account and clicking on 'Sell a Car."},
        {"question": "Is there a listing fee?", "answer": "No, listing your car is completely free. "},
        {"question": "Can I contact the seller directly?", "answer": "Yes, each listing includes contact information."},
        {"question": "Are the cars inspected?", "answer": "We recommend inspection, but it’s up to buyers to verify condition."},
        {"question": "Can I edit my listing?", "answer": "Yes, just go to 'My Listings' in your dashboard."},
    ]
    random.shuffle(faqs)
    return render(request, 'users/fandq.html', {'faqs': faqs})

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        full_message = f"From: {name} <{email}>\n\n{message}"

        send_mail(
            subject,
            full_message,
            settings.DEFAULT_FROM_EMAIL,
            ['minthwayhtut568@gmail.com'],
            fail_silently=False,
        )
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact')

    return render(request, 'users/contact.html')


def splash_view(request):
    return render(request, 'users/splash-screen.html')

def car_list(request):
    car_list = Car.objects.all().order_by('-id')
    paginator = Paginator(car_list, 8)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'home.html', {'page_obj': page_obj})

def generate_data(request):
    for i in range(0, 100):
        CarBrandNames.objects.create(car_brand_names=fake.address())
    return JsonResponse({'status': 200})


def search_car_brand_names(request):
    car_brand_names = request.GET.get('car_brand_names')
    payload = []
    if car_brand_names:
        fake_address_objs = CarBrandNames.objects.filter(car_brand_names__icontains=car_brand_names)
    
        for fake_address_obj in fake_address_objs:
            payload.append(fake_address_obj.car_brand_names)

    return JsonResponse({'status':200, 'data': payload})

