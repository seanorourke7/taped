# Generated by Django 3.2.23 on 2024-02-09 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_custom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='custom',
            field=models.TextField(blank=True, null=True),
        ),
    ]
