# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shelf', '0003_auto_20150916_1609'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name_plural': 'authors', 'ordering': ('last_name', 'first_name'), 'verbose_name': 'author'},
        ),
        migrations.AlterField(
            model_name='author',
            name='first_name',
            field=models.CharField(verbose_name='first_name', max_length=20),
        ),
    ]
