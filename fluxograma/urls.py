from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.list_flux, name='list'),
    url(r'^create/$', views.create_flux, name='create'),
    url(r'^(?P<pk>[0-9]+)/$', views.detail_flux, name='detail'),
]
