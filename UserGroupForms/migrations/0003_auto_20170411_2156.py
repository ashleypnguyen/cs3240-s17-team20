# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('UserGroupForms', '0002_auto_20170411_1959'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='add_members',
        ),
        migrations.RemoveField(
            model_name='group',
            name='group_email',
        ),
        migrations.RemoveField(
            model_name='group',
            name='group_name',
        ),
        migrations.RemoveField(
            model_name='group',
            name='group_password',
        ),
        migrations.RemoveField(
            model_name='group',
            name='remove_members',
        ),
        migrations.AddField(
            model_name='group',
            name='group',
            field=models.OneToOneField(default=django.utils.timezone.now, to='auth.Group'),
            preserve_default=False,
        ),
    ]
