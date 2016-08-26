from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'my_polls_site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'polls.views.index', name='index'),
    url(r'^quiz/', 'polls.views.polls', name='polls'),
    url(r'^account/', include('registration.backends.default.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
