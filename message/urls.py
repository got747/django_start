from django.conf.urls import url

from message.views import MessageCreate
from . import views

urlpatterns = [
    url(r'^$', MessageCreate.as_view(), name='message'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^message/', MessageCreate.as_view(), name='message'),

]
