# Generated by Django 2.2.dev20190110235441 on 2019-01-18 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buisness',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buisness_name', models.CharField(max_length=200)),
                ('GPS_X', models.FloatField(default=0)),
                ('GPS_Y', models.FloatField(default=0)),
                ('address', models.CharField(max_length=200)),
                ('student_discount', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=200)),
            ],
        ),
    ]