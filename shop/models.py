from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
from django.contrib.admin import display
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name=_("Başlıq"))
    slug = models.SlugField(unique=True, max_length=100, blank=True, null=True, verbose_name=_("Kategoriya URL"))
    
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
        
    def __str__(self):
        return self.title


    class Meta:
        verbose_name = _("Kategoriya")
        verbose_name_plural = _("Kategoriyalar")
        unique_together = ('title',)
        
        
        
    
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="product", verbose_name=_("Kategoriya"))
    title = models.CharField(max_length=150, verbose_name=_("Başlıq"))
    description = models.TextField(verbose_name=_("Təsvir"))
    price = models.IntegerField(default=0, validators=[MinValueValidator(0)], verbose_name=_("Qiymət"))
    slug = models.SlugField(unique=True, max_length=200, blank=True, verbose_name=_("Məhsul URL"))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Yaradılma Tarixi"))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("Yenilənmə Tarixi"))


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    
    def __str__(self):
        return self.title
        
        
    class Meta:
        verbose_name = _("Məhsul")
        verbose_name_plural = _("Məhsullar")
        unique_together = ('title',)
        
        
        
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images", verbose_name=_("Məhsul"))
    image = models.ImageField(upload_to="products/", verbose_name="Şəkil")
    order = models.IntegerField(validators=[MinValueValidator(0)], verbose_name=_("Öncəlik Sırası"))
    
    
    def __str__(self):
        return self.product.title
    
    
    @display(description=_("Mövcud Şəkil"))
    def image_tag(self):
        return format_html(f'<img width="150" src="{self.image.url}">')

    
    
    class Meta:
        verbose_name = _("Məhsul Şəkili")
        verbose_name_plural = _("Məhsul Şəkilləri")