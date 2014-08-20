# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bobo', '0002_auto_20140820_1438'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='school',
            name='country',
        ),
    ]
