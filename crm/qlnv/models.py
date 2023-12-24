from django.db import models
from django.urls import reverse

class LoaiNhanVien(models.Model):
    name = models.CharField(max_length=250,db_index=True)

    class Meta:
        verbose_name_plural ='LoaiNhanVien'

    def __str__(self):
        return  self.name

class NhanVien (models.Model):

    loaiNhanVien = models.ForeignKey(LoaiNhanVien,related_name='nhanvien', on_delete=models.CASCADE , null=True)
    maNV =  models.TextField(blank=True)
    tenNV =  models.TextField(blank=True)
    luongCB = models.DecimalField(max_digits=100, decimal_places=2)
    luongHT =models.DecimalField(max_digits=100, decimal_places=2 ,default=0.0,blank=True,null=True)
    
        
    class Meta:
        
        verbose_name_plural = ("NhanVien")

    def __str__(self):
        return self.tenNV


