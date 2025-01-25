from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.db.models import Q
from courses.models import Course

def homepage(request):
    courses = Course.objects.all()
    return render(request, 'index.html', {'courses': courses})

def search_courses(request):
    query = request.GET.get('q', '')
    courses = Course.objects.filter(
        Q(title__icontains=query) | Q(description__icontains=query)
    )[:5]
    return JsonResponse([{
        'id': course.id, 
        'title': course.title
    } for course in courses], safe=False)

