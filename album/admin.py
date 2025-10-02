from django.contrib import admin
from .models import ObraArte

@admin.register(ObraArte)
class ObraArteAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'artista', 'year', 'likes', 'created')
    search_fields = ('titulo', 'artista')
    list_filter = ('year', 'created')
    readonly_fields = ('created', 'updated')