# Generated by Django 5.0 on 2023-12-12 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_customer_store_custo_last_na_2e448d_idx'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='unit_price',
        ),
    ]