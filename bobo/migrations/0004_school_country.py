# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bobo', '0003_remove_school_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='country',
            field=models.CharField(max_length=50, default='country_default'),
            preserve_default=False,
        ),
    ]
