from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('<int:course_id>/', views.course_detail, name='course_detail'),
    path('<int:course_id>/unit/<int:unit_id>/lesson/<int:lesson_id>/', views.lesson_detail, name='lesson_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
