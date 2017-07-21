# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20170721_0902'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ptype',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='type', max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='ptype',
            field=models.ForeignKey(default=10, to='order.Ptype'),
            preserve_default=False,
        ),
    ]
