from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name="courses")

    def get_absolute_url(self):
        return reverse('course_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

class Unit(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="units")
    title = models.CharField(max_length=200)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.course.title} - {self.title}"

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="lessons")
    title = models.CharField(max_length=200)
    content = RichTextField()  # Supports rich text editing
    video_url = models.URLField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)  # To order lessons within a course
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name="lessons")

    class Meta:
        ordering = ['order']

    def get_absolute_url(self):
        return reverse('lesson_detail', kwargs={'pk': self.pk})

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

