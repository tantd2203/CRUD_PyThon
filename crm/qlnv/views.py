from django.shortcuts import render, get_object_or_404, redirect
from .models import LoaiNhanVien, NhanVien
from .forms import NhanVienForm  
from decimal import Decimal
def nhanvien_list(request):
    dsNhanVien = NhanVien.objects.all()
    dsLoaiNV = LoaiNhanVien.objects.all()
    return render(request, 'nhanvien_list.html', {'dsNhanVien': dsNhanVien,'dsLoaiNV': dsLoaiNV})

def nhanvien_detail(request, pk):
    nhanvien = get_object_or_404(NhanVien, pk=pk)
    return render(request, 'nhanvien_detail.html', {'nhanvien': nhanvien})


def nhanvien_create(request):
    if request.method == 'POST':
        maNV = request.POST.get('maNV')
        tenNV = request.POST.get('tenNV')
        luongCB= request.POST.get('luongCB')
        luongHT = request.POST.get('luongHT')
        loaiNhanVien = request.POST.get('loaiNhanVien')
        if (loaiNhanVien=="1"):
            luongHT =  Decimal(luongCB)*2
        elif (loaiNhanVien=="2"):
            luongHT =  Decimal(luongCB) *3
        nhanvien = NhanVien.objects.create(maNV= maNV,tenNV =tenNV ,luongCB= luongCB,luongHT= luongHT,loaiNhanVien_id= loaiNhanVien)
        return redirect('nhanvien_list')
    return render(request, 'nhanvien_list.html')


def nhanvien_edit(request, pk):
    nhanvien = get_object_or_404(NhanVien, pk=pk)
    if request.method == 'POST':
        form = NhanVienForm(request.POST, instance=nhanvien)
        if form.is_valid():
            nhanvien = form.save()
            return redirect('nhanvien_list')
    else:
        form = NhanVienForm(instance=nhanvien)
    return render(request, 'nhanvien_form.html', {'form': form})


def nhanvien_delete(request, pk):
    nhanvien = get_object_or_404(NhanVien, pk=pk)
    nhanvien.delete()
    return redirect('nhanvien_list')
