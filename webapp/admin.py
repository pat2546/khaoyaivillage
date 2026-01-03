from django.contrib import admin
from .models import School, SchoolImage

# ทำให้สามารถเพิ่มรูปภาพหลายใบในหน้าเดียวได้ (TabularInline)
class SchoolImageInline(admin.TabularInline):
    model = SchoolImage
    extra = 5 # เพิ่มช่องว่างให้อัปโหลดทีละ 5 รูป

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_info')
    inlines = [SchoolImageInline] # เอา SchoolImage ไปรวมไว้ในหน้าเพิ่ม School