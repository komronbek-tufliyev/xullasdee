# Generated by Django 4.2.4 on 2023-09-12 04:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_added_botuser_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='botuser',
            name='full_name_en',
        ),
        migrations.RemoveField(
            model_name='botuser',
            name='full_name_ru',
        ),
        migrations.RemoveField(
            model_name='botuser',
            name='full_name_uz',
        ),
    ]
