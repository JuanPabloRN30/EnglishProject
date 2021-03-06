# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-07 00:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.CharField(max_length=100, null=True)),
                ('number_listening', models.BigIntegerField(default=0)),
                ('number_writing', models.BigIntegerField(default=0)),
                ('number_reading', models.BigIntegerField(default=0)),
                ('user_django', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('correct', models.NullBooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_video', models.CharField(max_length=500)),
                ('letter', models.CharField(max_length=10000)),
                ('name', models.CharField(max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='option',
            name='song',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebSite.Song'),
        ),
    ]
