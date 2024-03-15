from django.db import models
from django.utils.text import slugify
from django.contrib.admin import display
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _




class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name=_("Başlıq"))
    description = models.TextField(verbose_name=_("Təsvir"))
    image = models.ImageField(upload_to="article-image/", verbose_name=_("Şəkil"))
    slug = models.SlugField(max_length=250, unique=True, null=True, blank=True, verbose_name=_("Slug URL"))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Yaradılma Tarixi"))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("Yenilənmə Tarixi"))
    
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
        
    def __str__(self):
        return self.title


    class Meta:
        verbose_name = _("Məqalə")
        verbose_name_plural = _("Məqalələr")
        unique_together = ('title',)
    
    
    
class ArticleGallery(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="images", verbose_name=_("Məqalə"))
    image = models.ImageField(upload_to="article-images/", verbose_name=_("Qalereya Şəkli"))
    
    
    def __str__(self):
        return self.article.title
    
    
    @display(description=_('Mövcud Şəkil'))
    def image_tag(self):
        return format_html(f'<img width="150" src="{self.image.url}">')


    class Meta:
        verbose_name = _("Məqalə Şəkili")
        verbose_name_plural = _("Məqalə Şəkilləri")