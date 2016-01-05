from django.conf.urls import include, url
from gist import views

urlpatterns = [
    url(r'^$', views.IndexViews.as_view(), name='index'),
    url(r'^info/$', views.InfoViews.as_view(), name='info'),
    url(r'^post/$', views.PostViews.as_view(), name='post'),
]