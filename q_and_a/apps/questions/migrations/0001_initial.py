# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organisations', '0004_auto_20150328_0915'),
        ('candidates', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer', models.TextField(blank=True)),
                ('completed', models.BooleanField(default=False)),
                ('completed_timestamp', models.DateField(null=True)),
                ('candidate', models.ForeignKey(to='candidates.Candidate')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.CharField(max_length=100, blank=True)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('asked', models.BooleanField(default=False)),
                ('organisation', models.ForeignKey(to='organisations.Organisation')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(to='questions.Question'),
            preserve_default=True,
        ),
    ]
