from django import forms
from .models import Contact
from django.utils.translation import gettext_lazy as _



class ContactForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Contact
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': _('Ad Soyad')}),
            'email': forms.EmailInput(attrs={'placeholder': _('E-Poçt Ünvanı')}),
            'phone': forms.TextInput(attrs={'placeholder': _('Telefon Nömrəsi')}),
            'subject': forms.TextInput(attrs={'placeholder': _('Mövzu')}),
            'message': forms.Textarea(attrs={'placeholder': _('Mesajınız')}),
        }