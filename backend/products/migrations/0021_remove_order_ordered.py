# Generated by Django 4.2.3 on 2024-01-05 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0020_order_product_delete_ordereditems'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='ordered',
        ),
    ]
