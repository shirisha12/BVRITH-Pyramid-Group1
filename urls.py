from django.conf.urls import url
from faculty import views

urlpatterns = [ 
	url(r'^index$',views.index,name = 'index'),
	url(r'^base$',views.base,name = 'base'),
	url(r'^success$',views.success,name = 'success')

]


