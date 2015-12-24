from django.contrib import admin
from django.conf.urls import include, url
from django.contrib.auth import settings

urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('home.urls', namespace="home")),
    url(r'^game/', include('game.urls', namespace="game")),
    url(r'^information/', include('information.urls', namespace="information")),
    url(r'^member/', include('member.urls', namespace="member")),
    url(r'^thanks/', include('thanks.urls', namespace="thanks")),
    url(r'^agreement/', include('agreement.urls', namespace="agreement")),
    url(r'^ueditor/',include('DjangoUeditor.urls')),
]
