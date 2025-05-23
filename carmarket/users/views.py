from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from listings.forms import CarForm
from listings.models import Car
import random

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'users/signup.html', {'form': form})


@login_required
def home(request):
    query = request.GET.get('search', '')
    sort_order = request.GET.get('sort', '')

    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CarForm()

    cars = Car.objects.all()

    if query:
        cars = Car.objects.filter(title__icontains=query)

    if sort_order == 'price_asc':
        cars = cars.order_by('price')
    elif sort_order == 'price_desc':
        cars = cars.order_by('-price')

    return render(request, 'users/home.html', {'form': form, 'cars': cars})


def about(request):
    return render(request, 'users/about.html')

def fandq(request):
    faqs = [
        {"question": "How do I list my car for sale?", "answer": "You can list your car by creating an account and clicking on 'Sell a Car."},
        {"question": "Is there a listing fee?", "answer": "No, listing your car is completely free. "},
        {"question": "Can I contact the seller directly?", "answer": "Yes, each listing includes contact information."},
        {"question": "Are the cars inspected?", "answer": "We recommend inspection, but it’s up to buyers to verify condition."},
        {"question": "Can I edit my listing?", "answer": "Yes, just go to 'My Listings' in your dashboard."},
        {"question": "How long will my car listing remain active?", "answer": "Listings stay active for 30 days by default. You can renew them from your dashboard before they expire. "},
    ]
    random.shuffle(faqs)
    return render(request, 'users/fandq.html', {'faqs': faqs})