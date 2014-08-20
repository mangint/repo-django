# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bobo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='lastname',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='school_current',
            new_name='school',
        ),
        migrations.RemoveField(
            model_name='student',
            name='dob',
        ),
    ]
