from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('upload-record', views.uploadpage, name="uploadpage"),
    
    path('student-csv', views.student_csv, name="student_csv"),
    path('address-csv', views.address_csv, name="address_csv"),
    path('course-csv', views.course_csv, name="course_csv"),

    path('info', views.info),
    path('addr', views.addr),
    path('crs', views.crs),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)