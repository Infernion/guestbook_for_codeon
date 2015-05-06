# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('guestbook', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='guestbookmodel',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 6, 16, 12, 37, 143514), auto_now_add=True),
            preserve_default=False,
        ),
    ]
