from .models import HeroSlider, HomeAbout, About, AboutVideo, Offer, OurWork, StaticInfo
from modeltranslation.translator import TranslationOptions, register


@register(HeroSlider)
class HeroSliderTranslationOptions(TranslationOptions):
    fields = ("title",)
    
    
@register(HomeAbout)
class HomeAboutTranslationOptions(TranslationOptions):
    fields = ("title", "description")
    
    
@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ("title", "description")
    
    
@register(AboutVideo)
class AboutVideoTranslationOptions(TranslationOptions):
    fields = ("title",)
    
    
@register(Offer)
class OfferTranslationOptions(TranslationOptions):
    fields = ("title", "description")
    
    
@register(OurWork)
class OurWorkTranslationOptions(TranslationOptions):
    fields = ("description",)
    
    
@register(StaticInfo)
class StaticInfoTranslationOptions(TranslationOptions):
    fields = ("products_slogan", "footer_slogan")
    

