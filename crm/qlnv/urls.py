from django.urls import path

from .import views

urlpatterns = [
    path('dsNhanVien/', views.nhanvien_list, name='nhanvien_list'),
    path('nhanVien/<int:pk>/', views.nhanvien_detail, name='detail'),
    path('nhanVien/new/', views.nhanvien_create, name='create'),
    path('<int:pk>/edit/', views.nhanvien_edit, name='edit'),
    path('<int:pk>/delete/', views.nhanvien_delete, name='delete'),

]