# Generated by Django 3.1.1 on 2020-09-24 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_auto_20200923_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[(1, 'High'), (2, 'Medium'), (3, 'Low')], default=2, max_length=1),
        ),
        migrations.AlterField(
            model_name='task',
            name='time_for_completion',
            field=models.DurationField(default='00:00:00', help_text='Format: HH:MM:SS', verbose_name='Time needed to complete task'),
        ),
    ]
