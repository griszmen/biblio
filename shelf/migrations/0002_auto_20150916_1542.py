# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shelf', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='BookEdition',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('isbn', models.CharField(max_length=17)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='BookItem',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('catalog_number', models.CharField(max_length=30)),
                ('cover_type', models.CharField(choices=[('soft', 'Soft'), ('hard', 'Hard')], max_length=4)),
                ('edition', models.ForeignKey(to='shelf.BookEdition')),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.RemoveField(
            model_name='book',
            name='isbn',
        ),
        migrations.RemoveField(
            model_name='book',
            name='publisher',
        ),
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(to='shelf.Author'),
        ),
        migrations.AddField(
            model_name='bookedition',
            name='book',
            field=models.ForeignKey(to='shelf.Book'),
        ),
        migrations.AddField(
            model_name='bookedition',
            name='publisher',
            field=models.ForeignKey(to='shelf.Publisher'),
        ),
        migrations.AddField(
            model_name='book',
            name='categories',
            field=models.ManyToManyField(to='shelf.BookCategory'),
        ),
    ]
