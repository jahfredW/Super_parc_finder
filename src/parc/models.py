import slugify as slugify
from django.db import models
from django_google_maps import fields as map_fields
from django.template.defaultfilters import slugify
from django.contrib.auth import get_user_model
from django.urls import reverse
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill
from datetime import date
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



class Abus(models.Model):
    INAP = 'IN'
    INSULTES = 'IS'
    NUDITE = 'NU'
    INFOS_ERRONEES = 'ER'
    FAUX_COMPTE = 'FA'
    MOTIF_CHOICES = [
        (INAP, 'Contenu inapproprié'),
        (INSULTES, 'Insultes_propos choquants'),
        (NUDITE, 'Nudité'),
        (INFOS_ERRONEES, 'Informations erronées'),
        (FAUX_COMPTE, 'Faux comptes'),
    ]
    motif = models.CharField(
        max_length=2,
        choices=MOTIF_CHOICES,
        default=INAP,
    )

    parc_name = models.CharField(blank=True, max_length=20)
    contexte = models.TextField(blank=True)
    date = models.DateField(blank=True, auto_now_add=True)  # La date de création
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    traite = models.BooleanField(blank=True, editable=True)

    class Meta:
        ordering = ['-date'] #ordre d'affichage du plus récent au moins récent
        verbose_name = "Abu"


    def get_absolute_url(self):
        return reverse('parc:home')

    def __str__(self):
        return self.name



class Location(models.Model):
    name = models.CharField(max_length=50) # nom Propre du lieu
    slug = models.SlugField(max_length=255, unique=True, blank=True) # le slug
    address_1 = models.CharField(max_length=128) # la première partie de l'adresse
    precision = models.TextField(max_length=1000, blank=True) # eventuellement des précisions
    # permet de resizer une image, le top et evite de faire à la main.
    thumbnail = models.ImageField(blank=True, upload_to='parc')
    resize_thumbnail = ImageSpecField(source='thumbnail',
                                      processors=[ResizeToFill(100, 50)],
                                      format='JPEG',
                                      options={'quality': 60})

    city = models.CharField(max_length=64, default="Dunkerque") # la ville
    postal_code = models.CharField(max_length=5, default="59240") # Le code Postal
    created_on = models.DateField(blank=True, auto_now_add=True) # La date de création
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    # Auteur ( relation un à un avec utilisateur )

    # classe Meta
    class Meta:
        ordering = ['-created_on'] #ordre d'affichage du plus récent au moins récent
        verbose_name = "Parc" #nom d'affichage dans l'interface d'administration

    # fonction qui permet de récupérer l'adresse sous forme d'une chaine de carcatère en minuscule
    def adresse(self):
        self.adresse = f"{self.address_1},{self.postal_code},{self.city}"
        return self.adresse.lower().replace('é', 'e')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('parc:home')


