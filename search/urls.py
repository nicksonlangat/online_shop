from django.urls import path
from django.contrib import admin
from .views import (searchposts)

urlpatterns = [
     path(r'^$', searchposts, name='searchposts'),

]