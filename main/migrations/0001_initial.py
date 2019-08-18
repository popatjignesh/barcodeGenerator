# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(max_length=20, verbose_name=django.contrib.auth.models.User)),
                ('complain_type', models.CharField(max_length=20, choices=[(b'water', b'Water Resources'), (b'electricity', b'Electricity')])),
                ('title', models.CharField(max_length=50)),
                ('mobile_no', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
