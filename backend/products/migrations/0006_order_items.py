# Generated by Django 4.2.3 on 2024-01-03 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_remove_order_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.TextField(default=''),
        ),
    ]