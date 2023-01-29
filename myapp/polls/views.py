from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import Question,Choice
from django.urls import reverse

# Create your views here.
def index(request):
    #creating reasonable views
    latest_question_list = Question.objects.order_by('-pub_date')
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list':latest_question_list
    }
    return HttpResponse(template.render(context,request))

#Write more view,mms
def details(request,question_id):
    question = get_object_or_404(Question, pk = question_id)  
    return render(request,'polls/detail.html',{'question':question})

def results(request,question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/results.html',{'question':question})
def vote(request,question_id):
    #modify so that voting can take place
    question = get_object_or_404(Question,pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except(KeyError,Choice.DoesNotExist):
        return render(request,'polls/detail.html',{'question':question,
        'error_message':'Choice Does Not Exist'})
    else:
        selected_choice.votes += 1
        selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args = (question_id,)))


#my own views
def available_choices(request):
    #we are going to pass via the choice_set function
    prim_key_num = Question.objects.count()
    question_list = {}
    for pky in range(1,prim_key_num+1):
        curr_question = Question.objects.get(pk=pky)
        choice = curr_question.choice_set.all()
        question_list[curr_question] = choice


    #template = loader.get_template('polls/index.html')
    context = {
        'question_list':question_list.items(),
        #'choice_list':choice_list
    }
    return render(request,'polls/index.html',context)
    