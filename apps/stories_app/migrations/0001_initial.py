# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-21 01:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('loginReg_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('commentator', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='loginReg_app.User')),
            ],
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateTimeField(max_length=10)),
                ('location', models.CharField(max_length=255)),
                ('emotion', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('bard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stories', to='loginReg_app.User')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='story',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='stories_app.Story'),
        ),
    ]
