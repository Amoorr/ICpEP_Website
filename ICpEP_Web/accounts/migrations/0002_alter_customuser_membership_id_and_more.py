# Generated by Django 5.1.3 on 2024-12-05 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='membership_id',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='student_id',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
