from django.shortcuts import render
from .models import FarmInfo

def home(request):
    farms = FarmInfo.objects.all()
    return render(request, 'home.html', {'farms': farms})

def Farm_Products(request):
    return render(request, 'Farm_Products.html')

def farm_activities(request):
    return render(request, 'farm_activities.html')

def seminar(request):
    return render(request, 'seminar.html')

def workshop(request):
    return render(request, 'workshop.html')

def packages(request):
    return render(request, 'packages.html')

def contact(request):
    return render(request, 'contact.html')

def booking(request):
    return render(request, 'booking.html')