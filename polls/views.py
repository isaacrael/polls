from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from .models import Answer, Question
import random

# Create your views here.

"""

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def polls(request):
    return render(request, 'polls.html')

"""

"""
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = RequestContext(request, {
        'latest_question_list': latest_question_list,
    })
    return HttpResponse(template.render(context))
"""

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

"""
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)
"""


def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_answer = p.answer_set.get(pk=request.POST['answer'])
    except (KeyError, Answer.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        value = 0
        # value = random.randint(1,1000)
        selected_answer.votes = value + 1
        selected_answer.save()
        # Develop An Algorithm to zero out all of the votes
        #votes = 0
        #votes.save()
        #value = 0
        #selected_answer.votes = value
        #selected_answer.save()
        #answers = p.answer_set
        #answers.votes.save()
        #Answer.votes = str[0]
        #Answer.votes.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
