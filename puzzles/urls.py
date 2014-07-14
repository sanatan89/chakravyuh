'''
Created on 14-Jul-2014

@author: sanatan
'''

from django.conf.urls import patterns, url
from puzzles import views


urlpatterns = patterns('',
    url(r'^round/(?P<p_id>[0-9]+)/$',views.puzzle, name='puzzle'),
    )