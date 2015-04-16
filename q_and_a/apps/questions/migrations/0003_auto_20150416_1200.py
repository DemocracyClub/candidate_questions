# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_auto_20150330_2232'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='choices',
            field=models.CharField(max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='question',
            name='type',
            field=models.CharField(default=b'text', max_length=8, choices=[(b'text', b'text'), (b'bool', b'yes/no'), (b'options', b'multiple choice')]),
            preserve_default=True,
        ),
    ]
