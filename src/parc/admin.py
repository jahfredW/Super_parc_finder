from django.contrib import admin
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields
from parc.models import Parc

# Register your models here.

class ParcAdmin(admin.ModelAdmin):
    list_display = ['title',]
    formfield_overrides = {
        map_fields.AddressField: {
            'widget': map_widgets.GoogleMapsAddressWidget(attrs={'data-map-type': 'roadmap'})
        }
    }


admin.site.register(Parc, ParcAdmin)