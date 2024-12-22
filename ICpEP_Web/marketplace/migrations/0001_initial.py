# Generated by Django 5.1.3 on 2024-11-14 10:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tag', models.CharField(max_length=200)),
                ('quantity', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'Product',
                'ordering': ['product_name'],
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('cart_id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(default=0)),
                ('order_status', models.CharField(choices=[('Pending', 'Pending'), ('Received', 'Received')], default='Pending', max_length=20)),
                ('order_date', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketplace.product')),
            ],
            options={
                'db_table': 'Cart',
                'ordering': ['order_date'],
            },
        ),
    ]
