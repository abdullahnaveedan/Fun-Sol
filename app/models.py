from django.db import models

# Create your models here.

class studentinfo(models.Model):
    student_name = models.CharField(default = "", max_length=50)
    father_name = models.CharField(default = "", max_length=50)
    age = models.CharField(default = "", max_length=50)

    def __str__(self):
        return self.student_name
class address(models.Model):
    street = models.CharField(default = "", max_length=50)
    city = models.CharField(default = "", max_length=50)
    postal = models.CharField(default = "", max_length=50)
    student_name = models.OneToOneField(studentinfo, on_delete=models.CASCADE)
    def __str__(self):
        return self.city

class course(models.Model):
    course_id = models.CharField(default = "", max_length=50)
    course_name = models.CharField(default = "", max_length=50)
    cradit_hr = models.CharField(default = "", max_length=50)
    student_info = models.ForeignKey(studentinfo, on_delete=models.CASCADE)
    def __str__(self):
        return self.course_id
    
