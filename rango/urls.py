from django.conf.urls import url
from . import views

app_name='rango'
urlpatterns=[
    url('^$',views.index,name='index'),
    url('^category/(?P<category_name_slug>[\w\-]+)/$',views.show_category,name='show_category'),
]