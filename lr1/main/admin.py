from django.contrib import admin
from .models import Links


# admin.site.register(Links)

class LinksAdmin(admin.ModelAdmin):
    list_display = ('linkURL', 'counter')


admin.site.register(Links, LinksAdmin)
