from django.shortcuts import render, get_object_or_404
from .models import FarmInfo, School, SchoolImage

def home(request):
    farms = FarmInfo.objects.all()
    return render(request, 'home.html', {'farms': farms})

def csr(request):
    return render(request, 'csr.html')

def course(request):
    return render(request, 'course.html')

def reservation(request):
    return render(request, 'Reservation_schedule.html')

def location(request):
    return render(request, 'location.html')

def picture(request):
    # ดึงรายชื่อโรงเรียนไปแสดงในหน้า picture.html (รูปที่ 2)
    schools = School.objects.all()
    return render(request, 'picture.html', {'schools': schools})

def school_detail(request, school_id):
    # ดึงข้อมูลโรงเรียนและรูปภาพไปแสดงหน้าแกลเลอรี (รูปที่ 3)
    school = get_object_or_404(School, id=school_id)
    images = school.images.all()
    return render(request, 'school_detail.html', {'school': school, 'images': images})

def learning_center(request):
    return render(request, 'learning_center.html')

def one_day_trip(request):
    return render(request, 'one_day_trip.html')

def stem_camp(request):
    return render(request, 'stem_camp.html')

def farm_tour(request):
    return render(request, 'farm_tour.html')