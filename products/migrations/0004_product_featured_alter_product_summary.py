# Generated by Django 4.1.6 on 2023-06-28 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0003_alter_product_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="featured",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="summary",
            field=models.TextField(blank=True),
        ),
    ]