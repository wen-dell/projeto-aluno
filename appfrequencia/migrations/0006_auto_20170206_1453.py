# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-06 16:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appfrequencia', '0005_auto_20170206_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='matricula',
            field=models.IntegerField(default=0),
        ),
    ]