from .models import Category, Product
from modeltranslation.translator import TranslationOptions, register


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ("title",)
    
    
@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ("title", "description")