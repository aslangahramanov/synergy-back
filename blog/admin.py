from django.contrib import admin
from .models import Article, ArticleGallery
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TranslationAdmin





class ArticleGalleryInline(admin.TabularInline):
    model = ArticleGallery
    readonly_fields = ['image_tag']
    extra = 1




@admin.register(Article)
class ArticleAdmin(TranslationAdmin):
    list_display = ('title', 'short_description', 'formatted_created', 'display_image')
    search_fields = ['title']
    list_filter = ['title']
    readonly_fields = ['created', 'updated', 'slug']
    inlines = [ArticleGalleryInline]
    group_fieldsets = True

    def display_image(self, obj):
        return format_html('<img src="{}" width="140" height="100" />', obj.image.url) if obj.image else '-'
    display_image.short_description = _('Şəkil')
    
    def short_description(self, obj):
        return (obj.description[:50] + '...') if len(obj.description) > 50 else obj.description
    short_description.short_description = _('Təsvir')

    def formatted_created(self, obj):
        return obj.created.strftime('%d %b %Y')
    formatted_created.short_description = _('Yaradılma Tarixi')
    





