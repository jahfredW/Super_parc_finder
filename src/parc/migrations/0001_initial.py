# Generated by Django 4.0.3 on 2022-03-17 11:08

from django.db import migrations, models
import django_google_maps.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('adress', django_google_maps.fields.AddressField(max_length=200)),
                ('geolocalisation', django_google_maps.fields.GeoLocationField(max_length=100)),
            ],
        ),
    ]