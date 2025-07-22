from django.contrib import admin
from .models import User, Project, Link, Icon, Artist, Music

@admin.register(Icon)
class IconAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon']
    search_fields = ['name']

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ['name', 'url']
    search_fields = ['name', 'url']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'type_icon', 'links', 'get_description_preview']
    list_filter = ['type_icon']
    search_fields = ['name', 'description']
    
    def get_description_preview(self, obj):
        """Показываем краткое описание в списке"""
        if obj.description:
            return obj.description[:50] + '...' if len(obj.description) > 50 else obj.description
        return 'Без описания'
    get_description_preview.short_description = 'Описание'

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'count_projects']
    search_fields = ['username', 'email']


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = ['name', 'artist', 'time']
    search_fields = ['name', 'artist']