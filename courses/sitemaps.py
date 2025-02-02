from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Course, Lesson

class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = "weekly"

    def items(self):
        return ['homepage', 'search_courses', 'search_results']

    def location(self, item):
        return reverse(item)

class CourseSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Course.objects.all()

    def lastmod(self, obj):
        # Get the last modified lesson within a course
        last_lesson = Lesson.objects.filter(course=obj).order_by('-order').first()
        return last_lesson.order if last_lesson else None  # Handle cases where no lessons exist


class LessonSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.7

    def items(self):
        return Lesson.objects.all()

    def location(self, obj):
        return obj.get_absolute_url()  # This will now use the updated method

    def lastmod(self, obj):
        return obj.order if obj else None


