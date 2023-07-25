# Generated by Django 4.2.2 on 2023-06-18 07:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movie_orders', '0001_initial'),
        ('movies', '0002_movieorder_movie_movie_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='movie_order',
            field=models.ManyToManyField(related_name='movie_orders', through='movie_orders.MovieOrder', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='MovieOrder',
        ),
    ]
