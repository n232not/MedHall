from courses.models import Course

def courses_processor(request):
    courses_all = Course.objects.all()
    print(f"Context processor found {len(courses_all)} courses")  # Debug print
    return {
        'courses_all': courses_all
    }