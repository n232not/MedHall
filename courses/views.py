from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Course, Lesson
from django.http import JsonResponse
from django.db.models import Q

def homepage(request):
    courses = Course.objects.all()
    return render(request, 'index.html', {'courses': courses})

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    courses = Course.objects.all()  # Add this
    return render(request, 'courses/course_detail.html', {'course': course, 'courses': courses})

def lesson_detail(request, course_id, lesson_id):
    course = get_object_or_404(Course, id=course_id)
    lesson = get_object_or_404(Lesson, id=lesson_id, course=course)
    courses = Course.objects.all()  # Add this
    return render(request, 'courses/lesson_detail.html', {'lesson': lesson, 'courses': courses})


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})
