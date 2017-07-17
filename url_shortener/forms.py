from django import forms


from .models import URLRedirect


class URLRedirectForm(forms.ModelForm):

    url = forms.URLField(max_length=4096, label='', widget=forms.TextInput(attrs={'placeholder': 'URL'}))

    class Meta:
        model = URLRedirect
        fields = ['url']

    def __init__(self, *args, **kwargs):
        super(URLRedirectForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control input-lg'