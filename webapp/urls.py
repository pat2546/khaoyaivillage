from django.urls import path
from .views import (
    home, 
    Farm_Products, 
    farm_activities, 
    seminar, 
    workshop, 
    packages, 
    contact, 
    booking
)

urlpatterns = [
    path('', home, name='home'),
    path('farm_products/', Farm_Products, name='farm_products'),
    path('activities/', farm_activities, name='farm_activities'),
    path('seminar/', seminar, name='seminar'),
    path('workshop/', workshop, name='workshop'),
    path('packages/', packages, name='packages'),
    path('contact/', contact, name='contact'),
    path('booking/', booking, name='booking'),
]