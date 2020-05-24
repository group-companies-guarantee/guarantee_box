# Generated by Django 3.0.1 on 2020-05-24 21:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone', models.TextField(blank=True, default='79151761287', max_length=500)),
                ('city', models.CharField(default='', max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='TeacherStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TeacherSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_name', models.CharField(max_length=200)),
                ('student_name', models.CharField(max_length=200)),
                ('phone', models.TextField(blank=True, default='79151761287', max_length=500)),
                ('start_timestamp', models.DateTimeField()),
                ('end_timestamp', models.DateTimeField()),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.Teacher')),
            ],
        ),
        migrations.AddField(
            model_name='teacher',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='students.TeacherStatus'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.PositiveSmallIntegerField(default=0)),
                ('phone', models.TextField(blank=True, default='712312', max_length=500)),
                ('city', models.CharField(default='', max_length=60)),
                ('amount', models.IntegerField(default=0)),
                ('currency', models.CharField(default='RUB', max_length=3)),
                ('signup_confirmation', models.BooleanField(default=False)),
                ('status', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='students.StudentStatus')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
