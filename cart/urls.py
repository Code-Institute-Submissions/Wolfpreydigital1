from django.conf.urls import url
from .views import cart 


urlpatterns = [
    url(r'^$', cart, name='cart')
]