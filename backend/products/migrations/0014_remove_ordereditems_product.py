# Generated by Django 4.2.3 on 2024-01-04 06:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_remove_ordereditems_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordereditems',
            name='product',
        ),
    ]