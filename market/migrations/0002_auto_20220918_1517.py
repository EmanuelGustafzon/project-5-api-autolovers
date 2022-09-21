# Generated by Django 3.2.15 on 2022-09-18 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='market',
            name='country',
            field=models.CharField(default='none', max_length=200),
        ),
        migrations.AddField(
            model_name='market',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='market',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]