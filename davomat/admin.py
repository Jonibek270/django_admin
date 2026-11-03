from django.contrib import admin
from .models import *

@admin.register(Dates)
class DatesAdmin(admin.ModelAdmin):
    list_display = ['date','course']

@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'course']


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['student','date','is_present']