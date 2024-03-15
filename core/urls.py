from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from os import getenv
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
from django.views.i18n import set_language


urlpatterns = [
    path(getenv("ADMIN_URL") + '/', admin.site.urls),
    path('', include('info.urls')),
    path('', include('shop.urls')),
    path('', include('blog.urls')),
]


if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        re_path(r'^rosetta/', include('rosetta.urls'))
    ]
    
    
urlpatterns += i18n_patterns(
    *urlpatterns,
    prefix_default_language=True,
)


urlpatterns += [
    path("i18n/", include("django.conf.urls.i18n")),
]

    

    

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    



admin.site.index_title = _("SCUBO - İdarəetmə Paneli")
admin.site.site_title = _("SCUBO - İdarəetmə Paneli")
admin.site.site_header = _("SCUBO - İdarəetmə Paneli")