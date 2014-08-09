from django.shortcuts import HttpResponse, render, RequestContext,\
    render_to_response
from puzzles.models import Questions

def home(request):
    question = Questions.objects.get(id=1)
    p_id = 1
    slug = "what-is-the-capital-of-india"
    print question.slug
    print type(slug)
    return render_to_response('index.html',locals())