# Generated by Django 3.0.1 on 2020-06-16 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0020_auto_20200616_1652'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='salary_rate_duration',
            new_name='salary_rate_time_interval',
        ),
    ]