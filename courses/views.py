from django.shortcuts import render, get_object_or_404
from .models import Course, Lesson, Unit
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from supabase import create_client, Client

# Initialize Supabase client using settings
supabase = create_client(
    settings.SUPABASE_URL,
    settings.SUPABASE_SERVICE_KEY
)

@csrf_exempt
def ckeditor_image_upload(request):
    if request.method == "POST" and request.FILES.get("upload"):
        file = request.FILES["upload"]
        
        # Upload image to Supabase storage
        bucket_name = "ckeditor-images"
        file_name = file.name
        file_data = file.read()
        
        try:
            # Upload file to Supabase Storage
            response = supabase.storage.from_(bucket_name).upload(file_name, file_data)
            
            if hasattr(response, 'error') and response.error:
                return JsonResponse({"error": str(response.error)}, status=400)
            
            # Get the file URL
            file_url = f"{settings.SUPABASE_URL}/storage/v1/object/public/{bucket_name}/{file_name}"
            return JsonResponse({"url": file_url})
            
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    
    return JsonResponse({"error": "Invalid request"}, status=400)

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    courses = Course.objects.all()
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