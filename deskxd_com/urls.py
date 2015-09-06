from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('home.urls', namespace="home")),
    url(r'^game/', include('game.urls', namespace="game")),
    url(r'^contact/', include('contact.urls', namespace="contact")),
    url(r'^information/', include('information.urls', namespace="information")),
    url(r'^member/', include('member.urls', namespace="member")),
)
