# Generated by Django 3.0.1 on 2020-06-26 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('managers', '0003_manager_email'),
        ('students', '0004_student_student_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='responsible_manager',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='responsible_students', to='managers.Manager'),
            preserve_default=False,
        ),
    ]
