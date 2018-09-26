__author__ = 'yu'
__date__ = '2018/9/4 14:58'
from django.contrib import admin
from django.urls import path
from searchinfo import views
from django.conf.urls import url


urlpatterns = [
    url(r"^searchresult/$", views.searchResult),
]