from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse 
from .models import *
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
import csv

# Create your views here.

def index(request):
    param = {
        'students' : studentinfo.objects.all(),
        'address' : address.objects.all(),
        'course' : course.objects.all()
    }
    return render(request,"index.html", param)

def address_csv(request):
    data = address.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="address.csv"'
    csv_writer = csv.writer(response)
    for i in data:
        csv_writer.writerow([i.street, i.city, i.postal,i.student_name])
    return response

def student_csv(request):
    data = studentinfo.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="studentsinfo.csv"'
    csv_writer = csv.writer(response)
    for i in data:
        csv_writer.writerow([i.student_name, i.father_name, i.age])
    return response

def course_csv(request):
    data = course.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="course.csv"'
    csv_writer = csv.writer(response)
    for i in data:
        csv_writer.writerow([i.course_id, i.course_name, i.cradit_hr,i.student_info])
    return response

def uploadpage(request):
    return render(request , "uploadpage.html")

def info(request):
    if request.method == "POST":
        getfile = request.FILES['studentfile']
        switch = request.POST.get("switch")
        
        if not getfile.name.endswith('.csv'):
            return HttpResponse("<h1>Please upload a valid CSV file only.</h1>")
        try:
            csv_data = csv.reader(getfile.read().decode('utf-8').splitlines())
            if switch == "on":
                header = next(csv_data)
            for row in csv_data:
                st = studentinfo.objects.filter(student_name = row[0]).first()
                if not st:
                    studentinfo.objects.create(
                        student_name=row[0],
                        father_name=row[1],
                        age=row[2],
                    )
            return redirect("uploadpage")
        except Exception as e:
            return HttpResponse(f"Error processing CSV file: {str(e)}")
    return redirect("home")
def addr(request):
    if request.method == "POST":
        getfile = request.FILES['addressfile']
        switch = request.POST.get("switch")

        if not getfile.name.endswith('.csv'):
            return HttpResponse("<h1>Please upload a valid CSV file only.</h1>")

        try:
            csv_data = csv.reader(getfile.read().decode('utf-8').splitlines())
            if switch == "on":
                header = next(csv_data)

            for row in csv_data:  
                st = studentinfo.objects.filter(student_name = row[3]).first()
                if st:
                    existing_address = address.objects.filter(student_name=st).first()
                    if not existing_address:
                        address.objects.create(
                            street=row[0],
                            city=row[1],
                            postal=row[2],
                            student_name=st,
                        )
        except Exception as e:
            return HttpResponse(f"Error processing CSV file: {str(e)}")
    return redirect("home")

def crs(request):
    if request.method == "POST":
        getfile = request.FILES['coursefile']
        switch = request.POST.get("switch")
        
        if not getfile.name.endswith('.csv'):
            return HttpResponse("<h1>Please upload a valid CSV file only.</h1>")
        try:
            csv_data = csv.reader(getfile.read().decode('utf-8').splitlines())
            if switch == "on":
                header = next(csv_data)

            for row in csv_data:
                course_id = row[0]
                course_name = row[1]
                cradit_hr = row[2]
                student_name = row[3]
                st = studentinfo.objects.filter(student_name=student_name).first()
                if not st:
                    return HttpResponse(f"Error: Student '{student_name}' not found in the database.")
                existing_course = course.objects.filter(course_id=course_id).first()
                if not existing_course:
                    course.objects.create(
                        course_id=course_id,
                        course_name=course_name,
                        cradit_hr=cradit_hr,
                        student_info=st,
                )
        except Exception as e:
            return HttpResponse(f"Error processing CSV file: {str(e)}")
    return redirect("home")