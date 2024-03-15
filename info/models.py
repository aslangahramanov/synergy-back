from django.db import models
from bs4 import BeautifulSoup
from ckeditor.fields import RichTextField
from shop.models import Product
from django.utils.translation import gettext_lazy as _



class HeroSlider(models.Model):
    title = models.CharField(max_length=150, verbose_name=_("Başlıq"))
    image = models.ImageField(upload_to="banner-images/", verbose_name=_("Şəkil"))
    
    def __str__(self):
        return self.title
    
    
    class Meta:
        verbose_name = _("Slayder")
        verbose_name_plural = _("Slayderlər")



class HomeAbout(models.Model):
    title = models.CharField(max_length=100, verbose_name=_("Başlıq"))
    description = models.TextField(verbose_name=_("Təsvir"))
    image = models.ImageField(upload_to="home-about/", verbose_name=_("Şəkil"))

    def __str__(self):
        return self.title
    
    
    class Meta:
        verbose_name = _("Haqqımızda (Ana Səhifə)")
        verbose_name_plural = _("Haqqımızda (Ana Səhifə)")
    


class About(models.Model):
    title = models.CharField(max_length=150, verbose_name=_("Başlıq"))
    description = models.TextField(verbose_name=_("Təsvir"))
    image = models.ImageField(upload_to="about/", verbose_name=_("Şəkil"))
    
    
    def __str__(self):
        return self.title
    
    
    class Meta:
        verbose_name = _("Haqqımızda")
        verbose_name_plural = _("Haqqımızda")


class AboutVideo(models.Model):
    title = models.CharField(max_length=200, verbose_name=_("Başlıq"))
    url = models.TextField(null=True, blank=True, verbose_name=_("Video URL"))
    
    
    def __str__(self):
        return self.title



    class Meta:
        verbose_name = _("Haqqımızda (Video)")
        verbose_name_plural = _("Haqqımızda (Video)")
        
        


class ContactInfo(models.Model):
    mail = models.EmailField(max_length=100, verbose_name=_("E-Poçt"))
    phone = models.CharField(max_length=20, verbose_name=_("Telefon Nömrəsi"))
    address = models.CharField(max_length=100, verbose_name=_("Ünvan"))
    map_link = models.TextField(null=True, blank=False, verbose_name=_("Xəritə URL"))
    
    def save(self, *args, **kwargs):
        soup = BeautifulSoup(self.map_link, 'html.parser')
        iframe_tag = soup.find('iframe')
        if iframe_tag:
            src_attribute = iframe_tag.get('src')
            self.map_link = src_attribute
        super().save(*args, **kwargs)
        
        
    def __str__(self):
        return f"{self.mail} | {self.phone} | {self.address}"
        
        
    class Meta:
        verbose_name = _("Mağaza Əlaqə Məlumatları")
        verbose_name_plural = _("Mağaza Əlaqə Məlumatları")
        
    
    
class SocialMedia(models.Model):
    facebook = models.CharField(max_length=200, null=True, blank=True, verbose_name=_("Facebook URL"))
    twitter = models.CharField(max_length=200, null=True, blank=True, verbose_name=_("Tüitter URL"))
    youtube = models.CharField(max_length=200, null=True, blank=True, verbose_name=_("Youtube URL"))
    instagram = models.CharField(max_length=200, null=True, blank=True, verbose_name=_("İnstagram URL"))
    tiktok = models.CharField(max_length=200, null=True, blank=True, verbose_name=_("TikTok URL"))
    whatsapp = models.CharField(max_length=200, null=True, blank=True, verbose_name=_("Whatsapp URL"))
    linkedin = models.CharField(max_length=200, null=True, blank=True, verbose_name=_("Linkedin URL"))
    
    
    
    def __str__(self):
        return _("Sosial Media Hesabları")
    
    
    class Meta:
        verbose_name = _("Sosial Media Hesabları")
        verbose_name_plural = _("Sosial Media Hesabları")



class Contact(models.Model):
    full_name = models.CharField(max_length=100, verbose_name=_("Ad Soyad"))
    email = models.EmailField(max_length=100, verbose_name=_("E-Poçt"))
    phone = models.CharField(max_length=20, verbose_name=_("Telefon Nömrəsi"))
    subject = models.CharField(max_length=100, verbose_name=_("Mövzu"))
    message = models.TextField(verbose_name=_("Mesaj"))
    
    
    def __str__(self):
        return self.full_name
    
    
    class Meta:
        verbose_name = _("Müraciət")
        verbose_name_plural = _("Müraciətlər")



class Offer(models.Model):
    title = models.CharField(max_length=100, verbose_name=_("Başlıq"))
    description = models.TextField(verbose_name=_("Təsvir"))
    
    
    def __str__(self):
        return self.title
    
    
    class Meta:
        verbose_name = _("Təklif")
        verbose_name_plural = _("Təkliflər")



class OurWork(models.Model):
    description = models.TextField(verbose_name=_("Təsvir"))
    image = models.ImageField(upload_to="our-work/", verbose_name=_("Şəkil"))
    video_url = models.TextField(null=True, blank=True, verbose_name=_("Video URL"))
    
    
    def __str__(self):
        return _("İşlərimiz")
    
    
    class Meta:
        verbose_name = _("İşlərimiz")
        verbose_name_plural = _("İşlərimiz")
    



class StaticInfo(models.Model):
    header_logo = models.ImageField(upload_to="logo/", verbose_name=_("Header Loqo"))
    products_slogan = models.TextField(null=True, blank=True, verbose_name=_("Məhsullar Sloqanı"))
    product_pagination = models.IntegerField(default=3, null=True, blank=True, verbose_name=_("Səhifədəki Məhsulların Sayı"))
    article_pagination = models.IntegerField(default=3, null=True, blank=True, verbose_name=_("Səhifədəki Məqalələrin Sayı"))
    footer_logo = models.ImageField(upload_to="logo/", verbose_name=_("Footer Loqo"))
    footer_slogan = models.TextField(verbose_name=_("Footer Sloqanı"))
    
    
    def __str__(self):
        return _("Statik Məlumatlar")
    
    
    class Meta:
        verbose_name = _("Statik Məlumat")
        verbose_name_plural = _("Statik Məlumatlar")



class Statistic(models.Model):
    employees = models.IntegerField(default=0, verbose_name=_("Əməkdaşlar"))
    branches = models.IntegerField(default=0, verbose_name=_("Filiallar"))
    diversity = models.IntegerField(default=0, verbose_name=_("Məhsul Çeşidliliyi"))
    year_of_operation = models.IntegerField(default=0, verbose_name=_("Fəaliyyət İlləri"))
    
    
    def __str__(self):
        return _("Statistika")
    
    
    class Meta:
        verbose_name = _("Statistika")
        verbose_name_plural = _("Statistika")



class Partner(models.Model):
    title = models.CharField(max_length=100, verbose_name=_("Başlıq"))
    image = models.ImageField(upload_to="partners-logo/", verbose_name=_("Şəkil"))
    
    
    def __str__(self):
        return self.title
    
    
    class Meta:
        verbose_name = _("Partnyor")
        verbose_name_plural = _("Partnyorlar")




class Subscription(models.Model):
    mail = models.EmailField(max_length=100, verbose_name=_("E-Poçt"))
    
    
    def __str__(self):
        return self.mail
    
    
    class Meta:
        verbose_name = _("Abunə")
        verbose_name_plural = _("Abunələr")



class RecommendedProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='recommended', verbose_name=_("Məhsul"))
    
    
    def __str__(self):
        return self.product.title
    
    
    class Meta:
        verbose_name = _("Tövsiyə Olunan Məhsul")
        verbose_name_plural = _("Tövsiyə Olunan Məhsullar")