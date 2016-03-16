from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('qa.views',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', 'test', name='login'),
    url(r'^signup/', 'test', name='singup'),
    url(r'^question/(?P<id>\d+)/', 'test', name='question'),
    url(r'^ask/', 'test', name='ask'),
    url(r'^popular/', 'test', name='popular'),
    url(r'^new/', 'test', name='new'),
    url(r'^$', 'test')
)
