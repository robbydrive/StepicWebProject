from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

#    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', 'qa.views.log_in', name='login'),
    url(r'^signup/', 'qa.views.signup', name='singup'),
    url(r'^question/(?P<question_id>\d+)/', 'qa.views.question', name='question'),
    url(r'^ask/', 'qa.views.ask', name='ask'),
    url(r'^answer/', 'qa.views.answer', name='answer'),
    url(r'^popular/', 'qa.views.popular', name='popular'),
    url(r'^new/', 'qa.views.test', name='new'),
    url(r'^$', 'qa.views.main', name='home')
)
