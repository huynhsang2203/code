# Generated by Django 3.2.8 on 2021-10-29 07:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField(max_length=1000)),
                ('time_create', models.DateTimeField(default=datetime.datetime(2021, 10, 29, 7, 20, 52, 267909, tzinfo=utc))),
            ],
        ),
    ]
