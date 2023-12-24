from django.urls import path

from .import views

urlpatterns = [
    path('timkiemNV', views.timNV, name='timkiemNV'),
    path('maxluongHTsanxuat', views.search_nhanvien_max_luongHT_sanxuat, name='maxluongHTsanxuat'),
    path('timLuongHT', views.timLuongHT, name='timLuongHT'), 
    path('dsNhanVien/', views.nhanvien_list, name='nhanvien_list'),
    path('nhanVien/<int:pk>/', views.nhanvien_detail, name='detail'),
    path('nhanVien/new/', views.nhanvien_create, name='create'),
    path('<int:pk>/edit/', views.nhanvien_edit, name='edit'),
    path('<int:pk>/delete/', views.nhanvien_delete, name='delete'),

]