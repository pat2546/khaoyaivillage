from django.db import models

# --- ข้อมูลฟาร์ม ---
class FarmInfo(models.Model):
    # โค้ดเดิมของคุณ (เช่น name, description ฯลฯ)
    # หากมีฟิลด์อยู่แล้วให้ใส่กลับมาแทนที่ pass นะครับ
    pass 

# --- ระบบรูปภาพกิจกรรมโรงเรียน ---
class School(models.Model):
    name = models.CharField(max_length=255, verbose_name="ชื่อโรงเรียน")
    date_info = models.CharField(max_length=100, verbose_name="วันที่ทำกิจกรรม")
    logo = models.ImageField(upload_to='school_logos/', null=True, blank=True)

    def __str__(self):
        return self.name

class SchoolImage(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='school_galleries/')
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Image for {self.school.name}"

# --- ระบบบันทึกแบบฟอร์ม CSR ---
class CSRRequest(models.Model):
    activity = models.CharField(max_length=200, verbose_name="กิจกรรม")
    trip_type = models.CharField(max_length=100, verbose_name="ประเภททริป")
    date = models.DateField(null=True, blank=True, verbose_name="วันที่")
    guests = models.IntegerField(null=True, blank=True, verbose_name="จำนวนคน")
    name = models.CharField(max_length=255, verbose_name="ชื่อผู้ติดต่อ")
    phone = models.CharField(max_length=50, verbose_name="เบอร์โทรศัพท์")
    organization = models.CharField(max_length=255, verbose_name="องค์กร")
    email = models.EmailField(verbose_name="อีเมล")
    message = models.TextField(null=True, blank=True, verbose_name="ข้อความเพิ่มเติม")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# --- ระบบตารางการจอง (ที่เพิ่มใหม่) ---
class Booking(models.Model):
    title = models.CharField(max_length=255, verbose_name="ชื่อกลุ่ม/โรงเรียน")
    start_date = models.DateField(verbose_name="วันที่เริ่มกิจกรรม")
    end_date = models.DateField(verbose_name="วันที่สิ้นสุดกิจกรรม")
    booking_type = models.CharField(max_length=50, verbose_name="ประเภทกิจกรรม")
    color_code = models.CharField(max_length=10, default='#ff0000', verbose_name="รหัสสีแสดงผล")

    class Meta:
        db_table = 'webapp_booking' # บังคับให้ใช้ชื่อตารางเดียวกับใน MySQL ของคุณ

    def __str__(self):
        return self.title