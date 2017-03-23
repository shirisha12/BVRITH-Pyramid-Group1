from django.conf.urls import url
from app import views

urlpatterns = [ 
	url(r'^$',views.index,name = 'index'),
	url(r'^base$',views.base,name = 'base'),
	url(r'^success$',views.success,name = 'success')
]
