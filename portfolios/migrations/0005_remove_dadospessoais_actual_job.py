# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-05 18:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolios', '0004_auto_20160605_1826'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dadospessoais',
            name='actual_job',
        ),
    ]
