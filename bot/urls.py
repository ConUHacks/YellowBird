from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.query, name='query'),
    url(r'^result$', views.result, name='result'),
    url(r'^index', views.index, name='index'),
    url(r'^css/bootstrap.min.css', views.bootstrap, name='bootstrap'),
]