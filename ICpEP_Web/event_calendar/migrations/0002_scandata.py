# Generated by Django 5.1.3 on 2024-11-26 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_calendar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScanData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scanned_text', models.TextField()),
                ('scanned_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
