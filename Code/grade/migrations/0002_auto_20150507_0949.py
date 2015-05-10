# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('grade', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='lesson',
            field=models.ForeignKey(to='lesson.Lesson'),
        ),
        migrations.AddField(
            model_name='grade',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
