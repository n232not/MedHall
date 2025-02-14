# Generated by Django 5.1.5 on 2025-02-14 01:55

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_alter_course_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='description',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='content',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Content'),
        ),
    ]
