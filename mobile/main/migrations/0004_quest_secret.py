# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20151013_1324'),
    ]

    operations = [
        migrations.AddField(
            model_name='quest',
            name='secret',
            field=models.TextField(default='bla bla bla', help_text=b'the text diplayed to players when they complete the quest', verbose_name=b'secret informations'),
            preserve_default=False,
        ),
    ]
