from django.shortcuts import render, redirect
from .models import (HeroSlider, 
                     HomeAbout, 
                     About, 
                     AboutVideo, 
                     Offer, 
                     OurWork, 
                     Partner, 
                     Subscription, 
                     Statistic,
                     RecommendedProduct
                     )

from .forms import ContactForm
from django.contrib import messages
from shop.models import Product
from blog.models import Article
from django.utils.translation import gettext_lazy as _

from django.conf import settings

from django.urls import reverse
from django.http import HttpResponse
from django.utils import translation






def home(request):
    sliders = HeroSlider.objects.all()
    home_about = HomeAbout.objects.last()
    offers = Offer.objects.all()[:4]
    our_work = OurWork.objects.last()
    partners = Partner.objects.all()
    statistic = Statistic.objects.last()
    recommended_products = RecommendedProduct.objects.all()
    articles = Article.objects.all().order_by("-created")[:6]
    current_lang = translation.get_language()
    
    print(current_lang)
    user_language = 'az'
    translation.activate(user_language)
    response = HttpResponse()
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)
    print(current_lang)
    
    context = {
        'sliders': sliders,
        'home_about': home_about,
        'offers': offers,
        'partners': partners,
        'partners': partners,
        'our_work': our_work,
        'statistic': statistic,
        'recommended_products': recommended_products,
        'articles': articles,
        
    }
    
    if request.method == 'POST':
        mail = request.POST.get('mail')
        if mail:
            subscribe = Subscription.objects.create(mail=mail)
            subscribe.save()
            context['sub_success_message'] = _("Abunə olduğunuz üçün təşəkkülər ")
    
    return render(request, 'index.html', context=context)


def about(request):
    partners = Partner.objects.all()
    about = About.objects.last()
    about_video = AboutVideo.objects.last()

    
    context = {
        'partners': partners,
        'about': about,
        'about_video': about_video,
    }
    
    return render(request, 'about.html', context=context)


def contact(request):
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "contact.html", {'form': form, 'result': 'success'})
        else:
            return render(request, "contact.html", {'form': form, 'result': 'fail'})
    else:
        form = ContactForm()
        return render(request, 'contact.html', {'form': form, 'result': None})







def set_language(request, language):
    next_url = request.GET.get('next', '/')
    
    if language in [lang[0] for lang in settings.LANGUAGES]:
        request.session['django_language'] = language
        print("IF")
    else:
        print("ELSE")
        request.session['django_language'] = settings.LANGUAGE_CODE
    
    return redirect(next_url)