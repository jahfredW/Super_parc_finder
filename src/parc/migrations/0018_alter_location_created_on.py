# Generated by Django 4.0.3 on 2022-03-23 20:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parc', '0017_alter_location_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='created_on',
            field=models.DateField(blank=True, default=datetime.date(2022, 3, 23)),
        ),
    ]