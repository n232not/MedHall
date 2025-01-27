from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.db.models import Q
from courses.models import Course
from courses.models import Course, Unit, Lesson

def homepage(request):
    courses = Course.objects.all()
    return render(request, 'index.html', {'courses': courses})

def search_courses(request):
    print("search_courses called")
    query = request.GET.get('q', '')
    print(f"Search query received: {query}")
    if len(query) < 2:
        return JsonResponse({'results': []})

    courses = Course.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))[:2]
    units = Unit.objects.filter(title__icontains=query)[:2]
    lessons = Lesson.objects.filter(title__icontains=query)[:1]

    results = []
    for course in courses:
        results.append({
            'type': 'Course',
            'title': course.title,
            'url': f'/courses/{course.id}/'
        })
    for unit in units:
        results.append({
            'type': 'Unit',
            'title': unit.title,
            'url': f'/courses/{unit.course.id}/unit/{unit.id}/'
        })
    for lesson in lessons:
        results.append({
            'type': 'Lesson',
            'title': lesson.title,
            'url': f'/courses/{lesson.unit.course.id}/unit/{lesson.unit.id}/lesson/{lesson.id}/'
        })

    return JsonResponse({'results': results[:5]}, safe=False)

def search_results(request):
    print("search_results called")
    query = request.GET.get('q', '')
    
    courses = Course.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
    units = Unit.objects.filter(title__icontains=query)
    lessons = Lesson.objects.filter(title__icontains=query)
    
    return render(request, 'search_results.html', {
        'query': query,
        'courses': courses,
        'units': units,
        'lessons': lessons
    })