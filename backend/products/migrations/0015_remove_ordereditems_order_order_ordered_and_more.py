# Generated by Django 4.2.3 on 2024-01-04 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_remove_ordereditems_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordereditems',
            name='order',
        ),
        migrations.AddField(
            model_name='order',
            name='Ordered',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='products.ordereditems'),
        ),
        migrations.AddField(
            model_name='ordereditems',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_product_items', to='products.product'),
        ),
    ]
