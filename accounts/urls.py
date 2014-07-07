'''
Created on 06-Jul-2014

@author: sanatan
'''

from django.conf.urls import patterns, url
from accounts import views


urlpatterns = patterns('',
        url(r'^register/$',views.add_user, name='add_user'),
        url(r'^login/$',views.login_user, name='login_user'),
        url(r'^logout/$',views.logout_user, name='logout_user')
        )
