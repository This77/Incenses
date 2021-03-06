# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-10 09:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rauch', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='substanz',
            old_name='eigenschaften',
            new_name='eigenschaft_set',
        ),
        migrations.RemoveField(
            model_name='substanz',
            name='kaufdatum',
        ),
        migrations.AddField(
            model_name='substanz',
            name='aka',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='substanz',
            name='herkunft',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='substanz',
            name='tradition',
            field=models.CharField(blank=True, max_length=2048, null=True),
        ),
        migrations.AlterField(
            model_name='eigenschaft',
            name='bezeichnung',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='substanz',
            name='bezeichnung',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='substanz',
            name='name_botanisch',
            field=models.CharField(max_length=256),
        ),
    ]
