# Generated by Django 3.2.15 on 2022-09-20 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_rename_profileimage_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='experience_with_cars',
        ),
    ]
