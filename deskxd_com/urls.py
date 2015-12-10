from django.contrib import admin
from django.conf.urls import patterns, include, url
from django.contrib.auth import settings

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('home.urls', namespace="home")),
    url(r'^game/', include('game.urls', namespace="game")),
    url(r'^information/', include('information.urls', namespace="information")),
    url(r'^member/', include('member.urls', namespace="member")),
    url(r'^thanks/', include('thanks.urls', namespace="thanks")),
    url(r'^agreement/', include('agreement.urls', namespace="agreement")),
    url(r'^ueditor/',include('DjangoUeditor.urls')),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)
