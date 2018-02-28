from django.contrib import admin

from .models import Film, Venue, Screening


# Register your models here.

class FilmAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'director')

    fieldsets = (
        (None, {
        'fields': ('title', 'slug', 'description', 'director', 'image', 'trailer_embed')
        }),
        ('True/False Conversation', {
            'classes': ('collapse',),
            'fields': ('convo_author', 'convo_with', 'convo_text', 'convo_audio')
        }
        )
    )

class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')

admin.site.register(Film, FilmAdmin)
admin.site.register(Venue, VenueAdmin)
admin.site.register(Screening)