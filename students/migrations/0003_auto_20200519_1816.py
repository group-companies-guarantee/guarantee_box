# Generated by Django 3.0.6 on 2020-05-19 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20200519_1803'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentstatus',
            old_name='name_status',
            new_name='name',
        ),
    ]