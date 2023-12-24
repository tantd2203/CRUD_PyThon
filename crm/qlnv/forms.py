
from django import forms
from .models import NhanVien

class NhanVienForm(forms.ModelForm):
    class Meta:
        model = NhanVien
        fields = ['loaiNhanVien', 'maNV', 'tenNV', 'luongCB', 'luongHT']
