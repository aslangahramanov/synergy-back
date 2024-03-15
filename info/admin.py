from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TranslationAdmin


from .models import (
                        HeroSlider,
                        HomeAbout,
                        About,
                        AboutVideo,
                        ContactInfo,
                        SocialMedia,
                        Contact,
                        Offer,
                        OurWork,
                        StaticInfo,
                        Statistic,
                        Partner,
                        Subscription,
                        RecommendedProduct
                        )

    
    
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('mail',)
    search_fields = ['mail']
    readonly_fields = ['mail']
    
    
admin.site.register(Subscription, SubscriptionAdmin)
    
    

@admin.register(About)
class AboutAdmin(TranslationAdmin):
    list_display = ('title', 'short_description', 'display_image')
    
    
    def display_image(self, obj):
        return format_html('<img src="{}" width="140" height="100" />', obj.image.url) if obj.image else '-'
    display_image.short_description = _('Şəkil')
    
    
    def short_description(self, obj):
        return (obj.description[:50] + '...') if len(obj.description) > 50 else obj.description
    short_description.short_description = _('Təsvir')





@admin.register(HomeAbout)
class HomeAboutModel(TranslationAdmin):
    list_display = ('title', 'short_description', 'display_image')
    
    
    def display_image(self, obj):
        return format_html('<img src="{}" width="140" height="100" />', obj.image.url) if obj.image else '-'
    display_image.short_description = _('Şəkil')
    
    
    def short_description(self, obj):
        return (obj.description[:50] + '...') if len(obj.description) > 50 else obj.description
    short_description.short_description = _('Təsvir')





class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'subject')
    search_fields = ['full_name', 'email', 'phone']
    readonly_fields = ['full_name', 'email', 'phone', 'subject', 'message']


admin.site.register(Contact, ContactAdmin)





class PartnerAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_image')
    
    
    def display_image(self, obj):
        return format_html('<img src="{}" width="120" height="80" />', obj.image.url) if obj.image else '-'
    display_image.short_description = _('Şəkil')
    
    
admin.site.register(Partner, PartnerAdmin)





@admin.register(HeroSlider)
class HeroSliderAdmin(TranslationAdmin):
    list_display = ('title', 'display_image')
    group_fieldsets = True

    
    def display_image(self, obj):
        return format_html('<img src="{}" width="120" height="80" />', obj.image.url) if obj.image else '-'
    display_image.short_description = _('Şəkil')
    
    
    


@admin.register(Offer)
class OfferAdmin(TranslationAdmin):
    list_display = ('title', 'short_description')
    
    
    
    def short_description(self, obj):
        return (obj.description[:100] + '...') if len(obj.description) > 100 else obj.description
    short_description.short_description = _('Təsvir')








class RecommendedProductAdmin(admin.ModelAdmin):
    list_display = ('product_title', 'product_price', 'display_image')
    
    
    def display_image(self, obj):
        if obj.product.images.exists():
            return format_html('<img src="{}" width="100" height="100" />', obj.product.images.first().image.url)
        else:
            return '-'
    display_image.short_description = _('Şəkil')
    
    
    def product_title(self, obj):
        return obj.product.title
    
    def product_price(self, obj):
        return obj.product.price if obj.product.price != 0 else _("Razılaşma Yolu İlə")
    
    
admin.site.register(RecommendedProduct, RecommendedProductAdmin)





@admin.register(AboutVideo)
class AboutVideoAdmin(TranslationAdmin):
    list_display = ('title',)







@admin.register(StaticInfo)
class StaticInfoAdmin(TranslationAdmin):
    list_display = ('products_slogan',)







@admin.register(OurWork)
class OurWorkAdmin(TranslationAdmin):
    list_display = ('description',)





admin.site.register(ContactInfo)
admin.site.register(SocialMedia)
admin.site.register(Statistic)


