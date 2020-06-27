# Generated by Django 3.0.1 on 2020-06-27 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_student_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='source',
            field=models.CharField(choices=[('FB', 'Facebook'), ('VK', 'Vkontakte'), ('IN', 'Instagram')], default='FB', max_length=2),
        ),
    ]