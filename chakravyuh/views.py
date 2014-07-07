'''
Created on 06-Jul-2014

@author: sanatan
'''
from django.shortcuts import HttpResponse, render, RequestContext,\
    render_to_response


def home(request):
    return render_to_response('index.html',locals())
