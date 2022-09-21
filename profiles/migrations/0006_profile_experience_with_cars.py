# Generated by Django 3.2.15 on 2022-09-20 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_remove_profile_experience_with_cars'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='experience_with_cars',
            field=models.CharField(choices=[('no experience', 'No experience'), ('some experience', 'Some experience'), ('experienced', 'Experienced'), ('a lot of experience', 'A lot of experience'), ('professional expert', 'Professional expert')], default='none', max_length=30),
        ),
    ]