# Generated by Django 3.0.1 on 2020-06-16 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0017_auto_20200616_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessonroom',
            name='session_id',
            field=models.CharField(default='2_MX40Njc2OTMyNH5-MTU5MjMxNTU3NTcwNX5ZMlFHYTNWdTdJSDNFNnVTeUIyd09xU2F-UH4', max_length=100),
        ),
        migrations.AlterField(
            model_name='lessonroom',
            name='token',
            field=models.CharField(default='T1==cGFydG5lcl9pZD00Njc2OTMyNCZzaWc9YzdiZDZiN2Y3ZDZjMTBjOGRkZWZmMGMwMGRjMTc1ZDQ5N2VhM2NkYjpzZXNzaW9uX2lkPTJfTVg0ME5qYzJPVE15Tkg1LU1UVTVNak14TlRVM05UY3dOWDVaTWxGSFlUTldkVGRKU0RORk5uVlRlVUl5ZDA5eFUyRi1VSDQmY3JlYXRlX3RpbWU9MTU5MjMxNTU3NSZleHBpcmVfdGltZT0xNTkyNDAxOTc1JnJvbGU9cHVibGlzaGVyJm5vbmNlPTM2NTYzOSZpbml0aWFsX2xheW91dF9jbGFzc19saXN0PQ==', max_length=400),
        ),
    ]