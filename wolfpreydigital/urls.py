"""wolfpreydigital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""


from django.conf.urls import url, include
from django.contrib import admin
from accounts.views import index
from accounts import urls as accounts_urls
from home import urls as home_urls
from features import urls as urls_features
from pricing import urls as urls_pricing
from signin import urls as urls_signin
from blog import urls as urls_blog
from issues import urls as urls_issues
from cart import urls as urls_cart

urlpatterns = [
    url(r'^', include(home_urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/',include(accounts_urls)),
    url(r'^features/',include(urls_features)),
    url(r'^blog/',include(urls_blog)),
    url(r'^pricing/',include(urls_pricing)),
    url(r'^signin/',include(urls_signin)),
    url(r'^login/',include(accounts_urls)),
    url(r'^issues/',include(urls_issues)),
    url(r'^cart/',include(urls_cart)),
]
