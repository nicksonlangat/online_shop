from django.conf.urls import url
from django.urls import path
from . import views
from .views import SearchResultsView


app_name = 'shop'

urlpatterns = [
    url('search/', SearchResultsView.as_view(), name='search'),
    url(r'^$', views.product_list, name='product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
    
    
]