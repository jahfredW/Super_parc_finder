from django.contrib import admin
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields
from parc.models import Location
from django.contrib import admin
from imagekit.admin import AdminThumbnail

# Register your models here.

class ParcAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'thumbnail')
    list_editable = ('thumbnail',)
    admin_thumbnail = AdminThumbnail(image_field='thumbnail')
    formfield_overrides = {
        map_fields.AddressField: {
            'widget': map_widgets.GoogleMapsAddressWidget(attrs={'data-map-type': 'roadmap'})
        }
    }

admin.site.register(Location, ParcAdmin)

