# Generated by Django 4.0.3 on 2022-03-27 12:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_google_maps.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Adress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adress', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Parc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('adress', django_google_maps.fields.AddressField(max_length=200)),
                ('geolocalisation', django_google_maps.fields.GeoLocationField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
                ('address_1', models.CharField(max_length=128)),
                ('precision', models.TextField(blank=True, max_length=1000)),
                ('thumbnail', models.ImageField(blank=True, upload_to='parc')),
                ('city', models.CharField(default='Dunkerque', max_length=64)),
                ('postal_code', models.CharField(default='59240', max_length=5)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('author', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Parc',
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='Abus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motif', models.CharField(choices=[('IN', 'Contenu inapproprié'), ('IS', 'Insultes_propos choquants'), ('NU', 'Nudité'), ('ER', 'Informations erronées'), ('FA', 'Faux comptes')], default='IN', max_length=2)),
                ('parc_name', models.CharField(blank=True, max_length=20)),
                ('contexte', models.TextField(blank=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('traite', models.BooleanField(blank=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Abu',
                'ordering': ['-date'],
            },
        ),
    ]
