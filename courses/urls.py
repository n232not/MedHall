from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path

urlpatterns = [
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    path('course/<int:course_id>/unit/<int:unit_id>/', views.unit_detail, name='unit_detail'),
    path('course/<int:course_id>/unit/<int:unit_id>/lesson/<int:lesson_id>/', views.lesson_detail, name='lesson_detail'),
    path('ckeditor5/upload/', views.ckeditor_image_upload, name='ck_editor_5_upload_file'),  # Add this line
    path('', views.course_list, name='course_list'),
]