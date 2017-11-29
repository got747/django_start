from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^authorize/', views.authorize_view, name='authorize'),
    url(r'^registration/', views.registration_view, name='registration'),
]
