from django.conf.urls import url

from .views import HomeView, URLCreateView, ResultView

urlpatterns = [
    # url(r'^((?P<uuid>[\w-]+)?)$', HomeView.as_view(), name="index"),
    url(r'^result/(?P<unique_code>[\w-]+)$', ResultView.as_view(), name="result"),
    url(r'^create$', URLCreateView.as_view(), name="create"),
    url(r'^((?P<unique_code>[\w-]+)?)$', HomeView.as_view(), name="index"),
    
]


# www.example.com/((?P<uuid>[\w-]+)?)/
# www.example.com/create/
# www.example.com/results/