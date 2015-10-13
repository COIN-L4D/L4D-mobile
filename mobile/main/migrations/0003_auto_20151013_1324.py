# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20151012_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='context',
            name='quest',
            field=models.ForeignKey(default=None, blank=True, to='main.Quest', null=True),
        ),
        migrations.AlterField(
            model_name='context',
            name='state',
            field=models.CharField(default=b'PWD', max_length=3, null=True, blank=True, choices=[(b'PWD', b'Asking password'), (b'HAK', b'Hacking (mini-game)'), (b'SUC', b'Success (finished)')]),
        ),
        migrations.AlterField(
            model_name='quest',
            name='mini_game',
            field=models.ForeignKey(blank=True, to='main.MiniGame', help_text=b"the mini-game, don't set it for no hacking quest", null=True),
        ),
    ]
