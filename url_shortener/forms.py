from django import forms


from .models import URLRedirect


class URLRedirectForm(forms.ModelForm):
    class Meta:
        model = URLRedirect
        fields = ['url']