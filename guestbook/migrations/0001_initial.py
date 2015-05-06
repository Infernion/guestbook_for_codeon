# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GuestBookModel',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=250)),
                ('content', models.TextField(max_length=600)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
