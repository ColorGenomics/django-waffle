from __future__ import unicode_literals

from django.conf.urls import patterns, url

from waffle.views import wafflejs, flag_json

urlpatterns = patterns('',
    url(r'^wafflejs$', wafflejs, name='wafflejs'),
    url(r'^wafflejs/flags$', flag_json, name='wafflejs_flags'),
)
