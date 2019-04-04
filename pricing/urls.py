from django.conf.urls import url
from .views import pricing

urlpatterns = [
    url(r'^$', pricing, name='pricing')
]