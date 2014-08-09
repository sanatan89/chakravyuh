from django.conf.urls import patterns, url
from puzzles import views


urlpatterns = patterns('',
	url(r'^addquestion',views.add_question),
    url(r'^round/(?P<p_id>[0-9]+)/(?P<slug>[-\w+]+)/$',views.puzzle, name='puzzle'),
    )