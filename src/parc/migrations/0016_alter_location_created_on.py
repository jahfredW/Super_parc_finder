# Generated by Django 4.0.3 on 2022-03-23 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parc', '0015_alter_abus_options_rename_created_on_abus_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='created_on',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]