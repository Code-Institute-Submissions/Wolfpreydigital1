from django.conf.urls import url
from .views import blog

urlpatterns = [
    url(r'^$', blog, name='blog')
]