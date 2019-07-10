from django.shortcuts import render
from django.http import HttpResponse

from .models import Question

# Create your views here.
def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:3]
    output = 'last 3 question: ' + ', '.join([q.text for q in latest_questions])
    return HttpResponse(output)

def detail(requets, question_id):
    resp = f'You are looking for {question_id} questions detail'
    return HttpResponse(resp)

def results(request, question_id):
    resp = f'You are looking for {question_id} questions results'
    return HttpResponse(resp)

def vote(request, question_id):
    resp = f'You are voting on {question_id} question'
    return HttpResponse(resp)