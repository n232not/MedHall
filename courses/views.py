from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Course, Lesson, Unit
from django.http import JsonResponse
from django.db.models import Q

def homepage(request):
    courses = Course.objects.all()
    return render(request, 'index.html', {'courses': courses})

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    courses = Course.objects.all()  # Add this
    return render(request, 'courses/course_detail.html', {'course': course, 'courses': courses})

def unit_detail(request, course_id, unit_id):
    unit = get_object_or_404(Unit, id=unit_id, course_id=course_id)
    courses = Course.objects.all()
    return render(request, 'courses/unit_detail.html', {'unit': unit, 'courses': courses})

def lesson_detail(request, course_id, unit_id, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id, unit_id=unit_id, unit__course_id=course_id)
    courses = Course.objects.all()
    return render(request, 'courses/lesson_detail.html', {'lesson': lesson, 'courses': courses})


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})


