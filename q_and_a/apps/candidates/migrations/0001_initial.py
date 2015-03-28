# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('auth_token', models.CharField(db_index=True, max_length=255, blank=True)),
                ('popit_id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('contact_address', models.CharField(max_length=255, null=True, blank=True)),
                ('constituency_id', models.CharField(max_length=20)),
                ('constituency_name', models.CharField(max_length=64)),
                ('party', models.CharField(max_length=64, null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
