# Generated by Django 3.2.15 on 2022-09-13 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
        ('commentlikes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentlikes',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentlikes', to='comments.comment'),
        ),
    ]