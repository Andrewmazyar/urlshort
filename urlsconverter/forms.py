from django import forms
from .models import Urlshorter


class UrlForms(forms.ModelForm):
    class Meta:
        model = Urlshorter
        fields = ['url_long']