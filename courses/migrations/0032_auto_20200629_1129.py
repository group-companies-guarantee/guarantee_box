# Generated by Django 3.0.1 on 2020-06-29 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0031_auto_20200629_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessonroom',
            name='session_id',
            field=models.CharField(default='2_MX40Njc2OTMyNH5-MTU5MzQxOTM0OTYwMX5Sd1JiNUp3ZXFNTnJmWFZwM1piUEpMaFJ-UH4', max_length=100),
        ),
        migrations.AlterField(
            model_name='lessonroom',
            name='token',
            field=models.CharField(default='T1==cGFydG5lcl9pZD00Njc2OTMyNCZzaWc9ODM5MmU3MWI0NWJjNmMyMTE0ZGUyOGExYTJlMDhjYWRiYzNjODM2YTpzZXNzaW9uX2lkPTJfTVg0ME5qYzJPVE15Tkg1LU1UVTVNelF4T1RNME9UWXdNWDVTZDFKaU5VcDNaWEZOVG5KbVdGWndNMXBpVUVwTWFGSi1VSDQmY3JlYXRlX3RpbWU9MTU5MzQxOTM0OSZleHBpcmVfdGltZT0xNTkzNTA1NzQ5JnJvbGU9cHVibGlzaGVyJm5vbmNlPTgxNDQ4NCZpbml0aWFsX2xheW91dF9jbGFzc19saXN0PQ==', max_length=400),
        ),
    ]
