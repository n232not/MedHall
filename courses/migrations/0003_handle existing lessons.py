# courses/migrations/0002_add_unit_and_move_lessons.py
from django.db import migrations, models
import django.db.models.deletion

def create_default_units(apps, schema_editor):
    Course = apps.get_model('courses', 'Course')
    Unit = apps.get_model('courses', 'Unit')
    Lesson = apps.get_model('courses', 'Lesson')
    
    for course in Course.objects.all():
        default_unit = Unit.objects.create(
            course=course,
            title="Default Unit",
            order=0
        )
        Lesson.objects.filter(course=course).update(unit=default_unit)

class Migration(migrations.Migration):
    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('order', models.PositiveIntegerField(default=0)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='units', to='courses.course')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.AlterField(
            model_name='lesson',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='courses.course'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='unit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='courses.unit'),
        ),
        migrations.RunPython(create_default_units),
    ]