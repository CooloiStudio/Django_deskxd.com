from django.conf.urls import include, url
from gist import views

urlpatterns = [
    url(r'^$', views.IndexViews.as_view(), name='index'),
    url(r'^info/$', views.InfoViews.as_view(), name='info'),
    url(r'^updateinfo/$', views.UpdateInfoViews.as_view(), name='updateinfo'),
    url(r'^post/$', views.PostViews.as_view(), name='post'),
    url(r'^group/$', views.GroupViews.as_view(), name='group'),
    url(r'^create/$', views.create, name='create'),
    url(r'^update/$', views.update, name='update'),
    url(r'^create_group/$', views.create_group, name='create_group'),
]