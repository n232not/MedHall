"""
URL configuration for KhanAcademyClone project.
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from courses.sitemaps import StaticViewSitemap, CourseSitemap, LessonSitemap
from django.conf import settings
from django.conf.urls.static import static
from . import views

sitemaps = {
    'static': StaticViewSitemap(),
    'courses': CourseSitemap(),
    'lessons': LessonSitemap(),
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('courses/', include('courses.urls')),
    path('', views.homepage, name='homepage'),
    path('search/', views.search_courses, name='search_courses'),
    path('search/results/', views.search_results, name='search_results'),
    path('sitemap.xml', sitemap,
         {'sitemaps': sitemaps, 'template_name': 'custom_sitemap.xml'},
         name='django.contrib.sitemaps.views.sitemap'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)