# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-28 04:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mindthebyte', '0003_remove_molecule_drug'),
    ]

    operations = [
        migrations.AddField(
            model_name='molecule',
            name='Drug',
            field=models.BooleanField(default=True, verbose_name=b'Drug'),
        ),
    ]
