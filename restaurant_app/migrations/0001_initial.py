# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import restaurant_app.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
                ('description', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=40)),
                ('course', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('city', models.CharField(max_length=128)),
                ('reservation_date', models.DateField(default=restaurant_app.models.set_defualt_reservation_date)),
                ('phone_number', models.CharField(max_length=128)),
                ('guest_number', models.CharField(default=restaurant_app.models.set_default_guest_number, unique=True, max_length=128)),
                ('email', models.EmailField(max_length=128)),
                ('comment', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
                ('address', models.CharField(max_length=150)),
                ('telephone', models.CharField(unique=True, max_length=128)),
                ('photo_link', models.CharField(max_length=150)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='reservation',
            name='restaurant',
            field=models.ForeignKey(to='restaurant_app.Restaurant'),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='restaurant',
            field=models.ForeignKey(to='restaurant_app.Restaurant'),
        ),
    ]
