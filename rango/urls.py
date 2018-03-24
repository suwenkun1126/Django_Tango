from django.conf.urls import url
from . import views

app_name='rango'
urlpatterns=[
    url('^$',views.index,name='index'),
]