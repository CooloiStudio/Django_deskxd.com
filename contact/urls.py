from django.conf.urls import include, url
from contact import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
]