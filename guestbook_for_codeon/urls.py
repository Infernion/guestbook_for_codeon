from django.conf.urls import patterns, include, url
from django.contrib import admin

from guestbook.views import GuestBookView

urlpatterns = patterns('',
    url(r'^', GuestBookView.as_view(), name='index'),

)
