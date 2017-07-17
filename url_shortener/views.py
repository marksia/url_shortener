from django.urls import reverse
from django.views.generic import CreateView

from .forms import URLRedirectForm

class HomeView(CreateView):
	template_name = "index.html"
	form_class = URLRedirectForm

	def get_success_url(self):
		return reverse('url_shortener:index')
