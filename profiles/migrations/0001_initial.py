# Generated by Django 3.2.22 on 2024-02-20 19:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('default_phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('default_postcode', models.CharField(blank=True, max_length=20, null=True)),
                ('default_town_or_city', models.CharField(blank=True, max_length=40, null=True)),
                ('default_street_address1', models.CharField(blank=True, max_length=80, null=True)),
                ('default_street_address2', models.CharField(blank=True, max_length=80, null=True)),
                ('default_county', models.CharField(choices=[('Kildare', 'Kildare'), ('Dublin', 'Dublin'), ('Laois', 'Laois'), ('Carlow', 'Carlow'), ('Roscomman', 'Roscomman'), ('Kilkenny', 'Kilkenny'), ('Kerry', 'Kerry'), ('Galway', 'Galway'), ('Leitrim', 'Leitrim'), ('Wexford', 'Wexford'), ('Wicklow', 'Wicklow'), ('Waterford', 'Waterford'), ('Cork', 'Cork'), ('Sligo', 'Sligo'), ('Mayo', 'Mayo'), ('Limerick', 'Limerick'), ('Offaly', 'Offaly'), ('Meath', 'Meath'), ('Westmeath', 'Westmeath'), ('Donegal', 'Donegal'), ('Clare', 'Clare'), ('Louth', 'Louth'), ('Monaghan', 'Monaghan'), ('Tipperary', 'Tipperary'), ('Cavan', 'Cavan'), ('Longford', 'Longford')], default='Dublin', max_length=200)),
                ('default_country', models.CharField(blank=True, default='IE', max_length=2)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
