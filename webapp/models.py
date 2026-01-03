from django.db import models

class FarmInfo(models.Model):
    # โค้ดเดิมของคุณที่มีอยู่แล้ว
    pass 

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