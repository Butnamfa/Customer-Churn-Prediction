from django.contrib import admin
from django.urls import path, include
from mlapp import views  # นำเข้าฟังก์ชัน predict จาก mlapp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mlapp/', include('mlapp.urls')),  # เชื่อมโยงเส้นทาง mlapp
    path('predict/', views.predict, name='predict'),  # เส้นทาง /predict/ ที่ชี้ไปยังฟังก์ชัน predict
    path('', views.predict, name='home'),  # เส้นทางหลัก ('/') ชี้ไปที่ฟังก์ชัน predict ทันที
]
