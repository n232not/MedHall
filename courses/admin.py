from django.contrib import admin
from .models import Course, Lesson, Quiz, Progress, Unit

class LessonInline(admin.TabularInline):
   model = Lesson

class UnitInline(admin.TabularInline):
   model = Unit

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
   list_display = ('title', 'teacher')
   search_fields = ('title', 'description')
   inlines = [UnitInline]

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
   list_display = ('title', 'course', 'order')
   list_filter = ('course',)
   inlines = [LessonInline]

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
   list_display = ('title', 'unit')
   list_filter = ('unit',)
   search_fields = ('title', 'content')

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
   list_display = ('lesson', 'question')
   list_filter = ('lesson',)

@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
   list_display = ('student', 'lesson', 'completed')
   list_filter = ('completed',)