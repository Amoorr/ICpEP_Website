# Generated by Django 5.1.3 on 2024-12-05 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_calendar', '0002_scandata'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_venue',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
