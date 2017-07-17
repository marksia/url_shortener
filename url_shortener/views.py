from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.generic import CreateView, TemplateView
from django.views.generic.edit import FormView

from .models import URLRedirect

from .forms import URLRedirectForm


class HomeView(FormView):
	template_name = "index.html"
	form_class = URLRedirectForm

	def dispatch(self, request, *args, **kwargs):
		if self.kwargs.get('unique_code') is not None:
			# If unique code exists and object found in database, redirect user to its original url.
			try:
				url_object = URLRedirect.objects.get(unique_code=self.kwargs.get('unique_code'))
				return HttpResponseRedirect(url_object.url)
			except URLRedirect.DoesNotExist:
			# Redirect to home page if shortened URL does not exist.
				return HttpResponseRedirect("/")
		else:
			return super(HomeView, self).dispatch(request, *args, **kwargs)

	def get_success_url(self):
		return reverse('url_shortener:index')


class URLCreateView(CreateView):
	form_class = URLRedirectForm
	template_name = "index.html"

	def form_valid(self, form):

		url = form.instance.url
		try:
			self.object = URLRedirect.objects.get(url=url)
		except URLRedirect.DoesNotExist:
			return super(URLCreateView, self).form_valid(form)

		return HttpResponseRedirect(self.get_success_url())

	def get_success_url(self):
		return reverse('url_shortener:result', kwargs={'unique_code': self.object.unique_code})


class ResultView(TemplateView):
	template_name = "result.html"

	def get_unique_code(self):
		unique_code = self.kwargs["unique_code"]
		return unique_code


	def get_context_data(self, **kwargs):
		context = super(ResultView, self).get_context_data(**kwargs)
		context["result_url"] = "http://%s/%s" % (get_current_site(self.request), self.get_unique_code())
		return context

