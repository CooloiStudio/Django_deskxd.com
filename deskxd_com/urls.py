from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', include('home.urls', namespace="home")),
    url(r'^game/', include('game.urls', namespace="game")),
    url(r'^contact/', include('contact.urls', namespace="contact")),
    url(r'^information/', include('information.urls', namespace="information")),
    url(r'^member/', include('member.urls', namespace="member")),
)
