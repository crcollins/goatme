# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=400)),
                ('filename', models.CharField(max_length=50)),
                ('pdf', models.FileField(upload_to=b'articles')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
