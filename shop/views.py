from django.shortcuts import render
from .models import Category, Product, ProductImage
from info.models import StaticInfo, ContactInfo
from django.core.paginator import Paginator

# Create your views here.


def products(request):    
    # Sadəcə kateqoriya var deyə belə sadə yazdim. Əlavə filterlənmə olsaydı daha fərqli yazmaq mümkün idi.
    
    filter_category = request.GET.get('category')
    
    if filter_category:
        products = Product.objects.filter(category__slug=filter_category)
    else:
        products = Product.objects.all()
    
    
    
    # Admin paneldən səhifə bölgüsü qeyd olunubsa o saya uyğun hər səhifədə məhsul olacaq.
     
    static_pagination = StaticInfo.objects.last().product_pagination
     
    if static_pagination:
        paginator = Paginator(products, static_pagination)
    else:
        paginator = Paginator(products, 3)
    
    
    current_page = int(request.GET.get("page", 1)) 
    page = paginator.page(current_page)
    products = page.object_list
    
    context = {
        'products': products,
        'page': page,
        'paginator': paginator
    }
    
    return render(request, 'products.html', context=context)



def product_detail(request, pk, slug):
    product = Product.objects.get(pk=pk)
    product_images = product.images.all()
    phone_number = ContactInfo.objects.last().phone.replace(" ", "")[1:]
    
    
    # Mesajı admin paneldəndə əlavə etmək olardı. Spesifik olması üçün belə etdim.
    
    wp_message = f"""
    Salam "{product.title}" məhsulu ilə maraqlanıram. 
    """
    
    similar_products = Product.objects.filter(category=product.category).exclude(pk=pk)
    
    # Oxşar məhsullar hissəsini TrigramSimilarity ilə edirəm çox vaxt, 
    # postgresql qoşulmayıb deyə bu dəfəlik belə etdim. 
    
    
    
    context = {
        'product': product,
        'product_images': product_images,
        'phone_number': phone_number,
        'wp_message': wp_message,
        'similar_products': similar_products
    }
    
    return render(request, 'product-details.html', context=context)