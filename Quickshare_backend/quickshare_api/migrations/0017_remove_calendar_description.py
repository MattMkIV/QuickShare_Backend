# Generated by Django 4.1.3 on 2023-06-29 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quickshare_api', '0016_alter_calendar_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calendar',
            name='description',
        ),
    ]
