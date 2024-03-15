from django.shortcuts import render
from info.models import StaticInfo, ContactInfo
from .models import Article, ArticleGallery
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator



def blog(request):
    static_pagination = StaticInfo.objects.last().article_pagination
    
    articles = Article.objects.all()
    
    
    # Admin paneldən səhifə bölgüsü qeyd olunubsa o saya uyğun hər səhifədə məqalə olacaq.
    
    if static_pagination:
        paginator = Paginator(articles, static_pagination)
    else:
        paginator = Paginator(articles, 3)
        
    current_page = int(request.GET.get("page", 1)) 
    page = paginator.page(current_page)
    articles = page.object_list
    
    context = {
        'articles': articles,
        'page': page,
        'paginator': paginator,
    }
    
    return render(request, 'news.html', context=context)




def article(request, pk, slug):
    article = get_object_or_404(Article, pk=pk)
    last_articles = Article.objects.all().order_by('-created').exclude(pk=pk)[:6]
    gallery = ArticleGallery.objects.filter(article=article)
    
    context = {
        'article': article,
        'last_articles': last_articles,
        'gallery': gallery
    }
    
       
    return render(request, 'news-details.html', context=context)