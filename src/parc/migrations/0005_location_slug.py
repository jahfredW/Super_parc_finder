# Generated by Django 4.0.3 on 2022-03-17 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parc', '0004_alter_location_options_remove_location_address_2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True),
        ),
    ]