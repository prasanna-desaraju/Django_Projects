from django.shortcuts import render, HttpResponse
from .models import Student

def add_student(request):
    student = Student(name="Bob", age=21, email="bob25@example.com")
    student.save()
    return HttpResponse("Student record added successfully!")
def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})



