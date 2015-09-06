from django.conf.urls import include, url
from member import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
]