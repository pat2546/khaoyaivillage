from django.contrib import admin
# นำเข้า Model ทั้งหมดที่มีใน models.py เพื่อนำมาแสดงในหน้า Admin
from .models import FarmInfo, School, SchoolImage, CSRRequest, Booking

# --- 1. จัดการระบบรูปภาพกิจกรรมโรงเรียน ---
# ตั้งค่าให้สามารถอัปโหลดรูปภาพหลายใบพร้อมกันได้ในหน้าเดียว
class SchoolImageInline(admin.TabularInline):
    model = SchoolImage
    extra = 5  # แสดงช่องว่างให้อัปโหลดเพิ่มทีละ 5 รูป

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_info')  # แสดงชื่อโรงเรียนและวันที่ในหน้าตารางหลัก
    inlines = [SchoolImageInline]         # นำระบบอัปโหลดหลายรูปมารวมไว้ที่นี่

# --- 2. จัดการระบบตารางการจอง ---
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'booking_type') # แสดงคอลัมน์สำคัญ
    list_filter = ('booking_type', 'start_date') # เพิ่มตัวกรองด้านข้างเพื่อให้ค้นหาง่ายขึ้น

# --- 3. จัดการระบบแบบฟอร์ม CSR ---
@admin.register(CSRRequest)
class CSRRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'organization', 'activity', 'date', 'created_at')
    readonly_fields = ('created_at',) # ตั้งค่าให้อ่านได้อย่างเดียวสำหรับวันที่ส่งฟอร์ม

# --- 4. ข้อมูลฟาร์ม ---
admin.site.register(FarmInfo)