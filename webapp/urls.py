from django.urls import path
from .views import (
    home, course, csr, reservation, location, picture, school_detail,
    learning_center, one_day_trip, stem_camp, farm_tour # นำเข้า views ใหม่
)

urlpatterns = [
    path('', home, name='home'),
    path('course/', course, name='course'),
    path('learning-center/', learning_center, name='learning_center'),
    path('one-day-trip/', one_day_trip, name='one_day_trip'),
    path('stem-camp/', stem_camp, name='stem_camp'),
    path('farm-tour/', farm_tour, name='farm_tour'),
    path('csr/', csr, name='csr'),
    path('reservation/', reservation, name='reservation'),
    path('location/', location, name='location'),
    path('picture/', picture, name='picture'),
    path('school/<int:school_id>/', school_detail, name='school_detail'),
]