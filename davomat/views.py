from django.shortcuts import render, get_object_or_404, redirect
from .models import *


def date_list(request):
    dates=Dates.objects.all()
    context={'dates':dates}
    return render(request,'davomat/date_list.html',context)



def dates_with_course(request,id):
    find_courses=get_object_or_404(Courses,id=id)
    course=get_object_or_404(Courses,id=id)
    context={'courses':course}
    return render(request,'davomat/dates_with_course.html',context)



def course_detail(request,id):
    course=get_object_or_404(Courses,id=id)
    context={'course':course}
    return render(request,'davomat/course_detail.html',context)



def course_student(request,id):
    id=Courses.objects.get(id=id)
    student=Students.objects.filter(course=id)
    context={'student':student}
    return render(request,'davomat/course_student.html',context)


# Create your views here.
