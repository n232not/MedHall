from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from django.conf import settings
from .models import Course, Lesson

# For static pages
class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = "weekly"

    def items(self):
        return ['homepage', 'search_courses', 'search_results']

    def location(self, item):
        return reverse(item)

# For courses
class CourseSitemap(Sitemap):
    priority = 0.9
    changefreq = "weekly"

    def items(self):
        # Assuming you have a Course model
        return Course.objects.all()

    def location(self, obj):
        # Use reverse() with your URL pattern name
        return reverse('course_detail', kwargs={'course_id': obj.id})

# For lessons
class LessonSitemap(Sitemap):
    priority = 0.7
    changefreq = "daily"

    def items(self):
        # Assuming you have a Lesson model
        return Lesson.objects.all()

    def location(self, obj):
        return reverse('lesson_detail', kwargs={
            'course_id': obj.course.id,
            'unit_id': obj.unit.id,
            'lesson_id': obj.id
        })