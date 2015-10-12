# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Context',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('state', models.CharField(max_length=3, null=True, choices=[(b'PWD', b'Password'), (b'SUC', b'Success'), (b'HAK', b'Hacking')])),
            ],
        ),
        migrations.CreateModel(
            name='MiniGame',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Quest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('quest_type', models.CharField(max_length=3, choices=[(b'PWD', b'Password'), (b'ENI', b'Enigma'), (b'HAK', b'Hack')])),
                ('password', models.TextField(help_text=b'the password the player has to type if any, left it blank for hacking quest', blank=True)),
                ('enigma', models.TextField(help_text=b'the enigma to display to user, left it blank for no enigma quest', blank=True)),
                ('mini_game', models.ForeignKey(to='main.MiniGame', help_text=b"the mini-game, don't set it for no hacking quest", null=True)),
            ],
        ),
        migrations.AddField(
            model_name='context',
            name='quest',
            field=models.ForeignKey(to='main.Quest', null=True),
        ),
    ]
