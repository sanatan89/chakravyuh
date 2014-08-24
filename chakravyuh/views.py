from django.shortcuts import HttpResponse, render, RequestContext,\
    render_to_response
from puzzles.models import Questions
import logging
logger = logging.getLogger(__name__)

def home(request):
    try:
        question = Questions.objects.all()[0]
        p_id = question.id
        slug = question.slug
    except Exception as e:
        print "no check"
        logger.exception(str(e))
    #print question.slug
    #print type(slug)
    return render_to_response('index.html',locals())