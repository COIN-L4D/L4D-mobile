# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_quest_secret'),
    ]

    operations = [
        migrations.AddField(
            model_name='minigame',
            name='help_text',
            field=models.TextField(help_text=b'A text that helps the playerto understand the rules', blank=True),
        ),
        migrations.AlterField(
            model_name='minigame',
            name='name',
            field=models.CharField(max_length=120),
        ),
    ]
