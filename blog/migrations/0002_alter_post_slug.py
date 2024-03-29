# Generated by Django 3.2.22 on 2024-03-07 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, default='Must be unique for URL with no spaces. (match to title)', max_length=200, null=True, unique=True),
        ),
    ]
