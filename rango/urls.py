from django.conf.urls import url
from . import views

app_name='rango'
urlpatterns=[
    url('^$',views.index,name='index'),
    url('^add_category/$',views.add_category,name='add_category'),
    url('^category/(?P<category_name_slug>[\w\-]+)/add_page/$',views.add_page,name='add_page'),
    url('^category/(?P<category_name_slug>[\w\-]+)/$',views.show_category,name='show_category'),
]