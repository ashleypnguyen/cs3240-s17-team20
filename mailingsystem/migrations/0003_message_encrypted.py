# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailingsystem', '0002_message_read'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='encrypted',
            field=models.BooleanField(default=False),
        ),
    ]
