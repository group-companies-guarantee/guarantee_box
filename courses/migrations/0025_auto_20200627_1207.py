# Generated by Django 3.0.1 on 2020-06-27 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0024_auto_20200627_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessonroom',
            name='session_id',
            field=models.CharField(default='2_MX40Njc2OTMyNH5-MTU5MzI0ODgzMjg3OX5JcDJpdHlFZTNib0xTTDBWV0IvV3BiV2J-UH4', max_length=100),
        ),
        migrations.AlterField(
            model_name='lessonroom',
            name='token',
            field=models.CharField(default='T1==cGFydG5lcl9pZD00Njc2OTMyNCZzaWc9N2QzNjI5MzQxY2EwYWUxMjUwN2FkMmMwMmNmOGRkM2ZkY2YwM2E0YjpzZXNzaW9uX2lkPTJfTVg0ME5qYzJPVE15Tkg1LU1UVTVNekkwT0Rnek1qZzNPWDVKY0RKcGRIbEZaVE5pYjB4VFREQldWMEl2VjNCaVYySi1VSDQmY3JlYXRlX3RpbWU9MTU5MzI0ODgzMyZleHBpcmVfdGltZT0xNTkzMzM1MjMzJnJvbGU9cHVibGlzaGVyJm5vbmNlPTMwODk0MiZpbml0aWFsX2xheW91dF9jbGFzc19saXN0PQ==', max_length=400),
        ),
    ]
