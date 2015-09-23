# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shelf', '0004_auto_20150918_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookedition',
            name='book',
            field=models.ForeignKey(related_name='editions', to='shelf.Book'),
        ),
    ]
