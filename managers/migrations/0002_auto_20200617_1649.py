# Generated by Django 3.0.1 on 2020-06-17 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moneytransaction',
            name='comment',
            field=models.CharField(default='', max_length=200),
        ),
    ]
