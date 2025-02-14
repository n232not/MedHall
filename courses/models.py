from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.sites.models import Site

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = CKEditor5Field('Description', config_name='default')
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name="courses")

    def get_absolute_url(self):
        # Just return the path portion - the sitemap framework will handle the domain
        return reverse('course_detail', kwargs={'course_id': self.id})

    def __str__(self):
        return self.title

class Unit(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="units")
    title = models.CharField(max_length=200)
    order = models.PositiveIntegerField(default=0)
   
    def get_absolute_url(self):
        return reverse('unit_detail', kwargs={
            'course_id': self.course.id, 
            'unit_id': self.id
        })

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.course.title} - {self.title}"

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="lessons")
    title = models.CharField(max_length=200)
    content = CKEditor5Field('Content', config_name='default')
    video_url = models.URLField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name="lessons")

    def get_absolute_url(self):
        return reverse('lesson_detail', kwargs={
            'course_id': self.course.id,
            'unit_id': self.unit.id,
            'lesson_id': self.id
        })

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.course.title} - {self.title}"

class Quiz(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="quizzes")
    question = models.CharField(max_length=500)
    correct_answer = models.CharField(max_length=200)
    option_a = models.CharField(max_length=200)
    option_b = models.CharField(max_length=200)
    option_c = models.CharField(max_length=200)
    option_d = models.CharField(max_length=200)

    def __str__(self):
        return f"Quiz for {self.lesson.title}"

class Progress(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="progress")
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.username} - {self.lesson.title}"