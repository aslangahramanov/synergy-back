from django.contrib import admin
from .models import  Category, Product, ProductImage
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TranslationAdmin



@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ('title',)
    readonly_fields = ['slug']
    search_fields = ['title']
    group_fieldsets = True
    
    


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    readonly_fields = ['image_tag']
    extra = 1




@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display = ('title', 'short_description', 'custom_price', 'display_image')
    search_fields = ['title']
    list_filter = ['title', 'price']
    readonly_fields = ['created', 'updated', 'slug']
    inlines = [ProductImageInline]
    
    group_fieldsets = True
    
    
    

    def display_image(self, obj):
        if obj.images.exists():
            return format_html('<img src="{}" width="100" height="100" />', obj.images.first().image.url)
        else:
            return '-'
    display_image.short_description = _('Şəkil')

    
    
    def custom_price(self, obj):
        return _("Razılaşma Yolu İlə") if obj.price == 0 else obj.price


    def short_description(self, obj):
        return (obj.description[:50] + '...') if len(obj.description) > 50 else obj.description
    short_description.short_description = _('Təsvir')

