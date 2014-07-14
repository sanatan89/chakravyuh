from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse

# Create your views here.

@login_required
def puzzle(request, p_id=1):
    #print p_id
    return HttpResponse(p_id)