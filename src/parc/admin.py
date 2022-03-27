from django.contrib import admin
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields
from parc.models import Location, Abus
from django.contrib import admin
from imagekit.admin import AdminThumbnail

# Register your models here.

class ParcAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'thumbnail', 'author', 'address_1', 'postal_code', 'city')
    list_editable = ('thumbnail',)
    admin_thumbnail = AdminThumbnail(image_field='thumbnail')
    formfield_overrides = {
        map_fields.AddressField: {
            'widget': map_widgets.GoogleMapsAddressWidget(attrs={'data-map-type': 'roadmap'})
        }
    }


class AbusAdmin(admin.ModelAdmin):
    list_display = ('motif', 'contexte', 'date', 'author', 'parc_name','traite',)
    list_editable = ('traite', 'parc_name',)


admin.site.register(Location, ParcAdmin)
admin.site.register(Abus, AbusAdmin)
