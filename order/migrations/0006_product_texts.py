# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 08:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_product_music'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='texts',
            field=models.TextField(default=1, max_length=5000, verbose_name='文章'),
            preserve_default=False,
        ),
    ]
