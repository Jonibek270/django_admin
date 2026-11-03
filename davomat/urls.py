from django.urls import path
from .views import *



urlpatterns = [
    path('', date_list, name='date_list'),
    path('date_with_course/<uuid:id>/', dates_with_course, name='date_with_course'),
    path('course_detail/<uuid:id>/', course_detail, name='course_detail'),
    path('course_detail/<uuid:id>/', course_student, name='course_student'),
]