from django.conf.urls import include, url
from game import views

urlpatterns = [
    url(r'^$', views.IndexViews.as_view(), name='index'),
]