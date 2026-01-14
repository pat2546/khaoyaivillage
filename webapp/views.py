import json
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import FarmInfo, School, SchoolImage, CSRRequest, Booking # เพิ่ม Booking เข้ามา

def home(request):
    # รวมการทำงานของฟอร์ม CSR และการแสดงผลหน้าแรกไว้ด้วยกัน
    if request.method == 'POST':
        try:
            # รับข้อมูลจากฟอร์มใน base.html
            data = CSRRequest(
                activity = request.POST.get('activity'),
                trip_type = request.POST.get('trip_type'),
                date = request.POST.get('date') if request.POST.get('date') else None,
                guests = request.POST.get('guests') if request.POST.get('guests') else 0,
                name = request.POST.get('name'),
                phone = request.POST.get('phone'),
                organization = request.POST.get('org'),
                email = request.POST.get('email'),
                message = request.POST.get('message')
            )
            data.save()
            messages.success(request, 'ส่งข้อมูลเรียบร้อยแล้ว เจ้าหน้าที่จะติดต่อกลับโดยเร็วที่สุด')
            return redirect(request.META.get('HTTP_REFERER', 'home'))
        except Exception as e:
            messages.error(request, f'เกิดข้อผิดพลาด: {e}')
            return redirect('home')

    farms = FarmInfo.objects.all()
    return render(request, 'home.html', {'farms': farms})

def reservation(request):
    # ดึงข้อมูลการจองจากฐานข้อมูล MySQL (ตาราง webapp_booking)
    all_bookings = Booking.objects.all()
    
    # แปลงข้อมูลให้อยู่ในรูปแบบ List of Dictionary เพื่อทำ JSON
    events = []
    for booking in all_bookings:
        events.append({
            'title': booking.title,
            'start': booking.start_date.strftime("%Y-%m-%d"),
            'end': booking.end_date.strftime("%Y-%m-%d"),
            'backgroundColor': booking.color_code,
            'borderColor': booking.color_code,
            'allDay': True # ให้แสดงผลเป็นแถบยาว
        })
    
    # ส่งข้อมูลแบบ JSON ไปยังหน้า Reservation_schedule.html
    context = {
        'events_json': json.dumps(events)
    }
    return render(request, 'Reservation_schedule.html', context)

# ฟังก์ชันอื่นๆ คงเดิม
def csr(request):
    return render(request, 'csr.html')

def course(request):
    return render(request, 'course.html')

def location(request):
    return render(request, 'location.html')

def picture(request):
    schools = School.objects.all()
    return render(request, 'picture.html', {'schools': schools})

def school_detail(request, school_id):
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