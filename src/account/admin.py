from django.contrib import admin
from imagekit.admin import AdminThumbnail

from account.models import CustomUSer

class UserAdmin(admin.ModelAdmin):
    list_display = ('nom',)


admin.site.register(CustomUSer, UserAdmin)
# Attention ici toujours mettre le UserAdmin en deux.
