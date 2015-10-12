# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quest',
            name='password',
            field=models.CharField(help_text=b'the password the player has to type if any, left it blank for hacking quest', max_length=512, blank=True),
        ),
    ]
