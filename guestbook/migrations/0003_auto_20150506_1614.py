# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guestbook', '0002_guestbookmodel_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guestbookmodel',
            name='created',
            field=models.DateTimeField(auto_now=True),
            preserve_default=True,
        ),
    ]
