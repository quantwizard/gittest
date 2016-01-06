# from django.shortcuts import render

# # Create your views here.
from django.http import HttpResponse

'''
sort of handlers which take request as argument
to handle the request and give response
'''
def index(request):
    return HttpResponse("Hi, django")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
