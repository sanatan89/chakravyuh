from django.shortcuts import HttpResponse, render, RequestContext,\
    render_to_response
from puzzles.models import Questions
import logging
logger = logging.getLogger(__name__)

def home(request):
    try:
        question = Questions.objects.filter(p_id=1)
        p_id = 1
        slug = question.slug
    except Exception as e:
        logger.exception(str(e))
    #print question.slug
    #print type(slug)
    return render_to_response('index.html',locals())