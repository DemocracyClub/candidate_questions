# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('organisations', '0002_auto_20150302_1019'),
    ]

    operations = [
        migrations.AddField(
            model_name='organisation',
            name='user',
            field=models.OneToOneField(default='', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='organisation',
            name='auth_token',
            field=models.CharField(db_index=True, max_length=255, blank=True),
            preserve_default=True,
        ),
    ]
