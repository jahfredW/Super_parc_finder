import slugify as slugify
from django.db import models
from django_google_maps import fields as map_fields
from django.template.defaultfilters import slugify
from django.contrib.auth import get_user_model
# Create your models here.

class Parc(models.Model):
    title = models.CharField(max_length=50, blank=False)
    adress = map_fields.AddressField(max_length=200)
    geolocalisation = map_fields.GeoLocationField(max_length=100)

    def __str__(self):
        return self.title

class Adress(models.Model):
    adress = models.TextField(blank=True)

    def __str__(self):
        return self.adress

User = get_user_model()


class Location(models.Model):
    name = models.CharField(max_length=50)
    address_1 = models.CharField(max_length=128)
    precision = models.TextField(max_length=1000, blank=True)
    thumbnail = models.ImageField(blank=True, upload_to='blog')
    city = models.CharField(max_length=64, default="Zanesville")
    postal_code = models.CharField(max_length=5, default="59240")
    created_on = models.DateField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)


    class Meta:
        ordering = ['-created_on']
        verbose_name = "Parc"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)