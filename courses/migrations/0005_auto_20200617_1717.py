# Generated by Django 3.0.1 on 2020-06-17 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20200617_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='icon',
            field=models.ImageField(blank=True, default='', upload_to=''),
        ),
        migrations.AddField(
            model_name='course',
            name='old_cost',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=7),
        ),
        migrations.AddField(
            model_name='course',
            name='testimonial',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='course',
            name='testimonial_author',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='lessonroom',
            name='session_id',
            field=models.CharField(default='2_MX40Njc2OTMyNH5-MTU5MjQwMzQ1OTgzMX5NTDdTSEVicFBNOGNDWDF0WUZOblBoejd-UH4', max_length=100),
        ),
        migrations.AlterField(
            model_name='lessonroom',
            name='token',
            field=models.CharField(default='T1==cGFydG5lcl9pZD00Njc2OTMyNCZzaWc9NTliNGIyMGQ3ODgwMGY5NGI5ZmQ3MWU1NGM2M2RkNjZkYTMwNmJlNzpzZXNzaW9uX2lkPTJfTVg0ME5qYzJPVE15Tkg1LU1UVTVNalF3TXpRMU9UZ3pNWDVOVERkVFNFVmljRkJOT0dORFdERjBXVVpPYmxCb2VqZC1VSDQmY3JlYXRlX3RpbWU9MTU5MjQwMzQ1OSZleHBpcmVfdGltZT0xNTkyNDg5ODU5JnJvbGU9cHVibGlzaGVyJm5vbmNlPTkzMTEwNiZpbml0aWFsX2xheW91dF9jbGFzc19saXN0PQ==', max_length=400),
        ),
    ]
