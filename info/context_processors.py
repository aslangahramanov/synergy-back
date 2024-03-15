from .models import ContactInfo, SocialMedia, StaticInfo
from django.contrib import messages

def contact_info(request):
    contact_info = ContactInfo.objects.last()
    return {'contact_info': contact_info}


def static_info(request):
    static_info = StaticInfo.objects.last()
    return {'static_info': static_info}


def social_media(request):
    social_media = SocialMedia.objects.last()
    return {'social_media': social_media}

