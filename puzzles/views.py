from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from django.template.defaultfilters import slugify
from puzzles.forms import QuestionForm,AnswerForm
from puzzles.models import 	Questions


# Create your views here.

@csrf_exempt
def add_question(request):
    if request.method=="POST":
        form = QuestionForm(request.POST, request.FILES)
        #print request.FILES['image']
        if form.is_valid():
            print "valid"
            question = Questions.objects.create(
                    description=form.cleaned_data['description'],
                    level=form.cleaned_data['level'],
                    image=request.FILES['image'],
                    answer=form.cleaned_data['answer']
                    )
            question.save()
            #print "redirecting"
            return render(request,'index.html',locals())
        else:
            #print "eles"
            form=form
            return render(request, 'puzzles/add_question.html',locals())
    else:
        form = QuestionForm()
        return render(request,'puzzles/add_question.html',locals())
    pass

@csrf_exempt
#@login_required
def puzzle(request, p_id, slug):
    print "puzzle"
    q=Questions.objects.get(id=p_id)
    if request.method=="POST":
        print "inside post"
        form = AnswerForm(request.POST)
        if form.is_valid():
            print "valid"
            key = form.cleaned_data['key']
            print key
            print q.answer
            if key == q.answer:
                p_id=int(p_id)+1;
                q=Questions.objects.get(id=p_id)
                return HttpResponseRedirect(reverse('puzzles.views.puzzle', kwargs={'p_id':p_id ,'slug':q.slug}))
            else:
                form = AnswerForm()
                return render(request,'puzzles/level.html',locals())
        else:
            print "last block"
            form = form
            return render(request,'puzzles/level.html',locals())
    else:
        form = AnswerForm()
        return render(request,'puzzles/level.html',locals())
