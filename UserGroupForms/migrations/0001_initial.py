# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('group_name', models.CharField(max_length=20)),
                ('group_email', models.CharField(max_length=50)),
                ('group_password', models.CharField(max_length=30)),
                ('add_members', models.CharField(max_length=100)),
                ('remove_members', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('report_file_name', models.CharField(max_length=20)),
                ('report_file', models.FileField(upload_to='documents/')),
                ('company_name', models.CharField(max_length=50)),
                ('company_phone', models.CharField(max_length=11)),
                ('company_location', models.CharField(max_length=50)),
                ('company_country', models.CharField(max_length=20)),
                ('business_type', models.CharField(max_length=30)),
                ('current_projects', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('user_type', models.CharField(max_length=30)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
