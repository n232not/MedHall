# courses/sitemaps.py

from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Course, Lesson, Unit

class BaseSitemap(Sitemap):
    protocol = 'https'  # Force HTTPS

    def get_domain(self, site=None):
        # The site parameter is passed by Django's sitemap framework
        # We override it to return our custom domain
        return 'checkupbasic.com'  # or use environment variable to be more flexible

class StaticViewSitemap(BaseSitemap):
    priority = 0.8
    changefreq = "weekly"

    def items(self):
        return ['homepage', 'search_courses', 'search_results']

    def location(self, item):
        return reverse(item)

class CourseSitemap(BaseSitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Course.objects.all()

    def location(self, obj):
        return obj.get_absolute_url()

class LessonSitemap(BaseSitemap):
    priority = 0.7
    changefreq = "daily"

    def items(self):
        return Lesson.objects.all()

    def location(self, obj):
        return obj.get_absolute_url()