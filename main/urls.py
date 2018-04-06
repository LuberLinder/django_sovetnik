from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^o-kompanii/$', views.about, name='about'),
	url(r'^galereya/$', views.galary, name='galary'),
	url(r'^novosti/$', views.news, name='news'),
	url(r'^kontakty/$', views.contacts, name='contacts'),
	url(r'^thanks/$', views.thanks, name='thanks'),
]
