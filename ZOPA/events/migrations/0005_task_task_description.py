# Generated by Django 3.0.8 on 2020-09-23 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20200923_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_description',
            field=models.TextField(blank=True),
        ),
    ]