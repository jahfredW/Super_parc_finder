# Generated by Django 4.0.3 on 2022-03-24 21:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parc', '0022_alter_location_postal_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='commentaire',
        ),
    ]
