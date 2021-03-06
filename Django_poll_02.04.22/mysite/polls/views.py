from django import template
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.urls import reverse
from django.views import generic

from .models import Question, Choice
from django.utils import timezone


# Create your views here.

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        # zwróć 5 ostatnich pytań
        return User.objects.get(username="Wojciech").profile.my_field

        # # zwróć 5 ostatnich pytań
        # return Question.objects.filter(
        #     pub_date__lte=timezone.now()
        # ).order_by('-pub_date')[:5]


def QuestionList(request, question_type):
    latest_question_list = Question.objects.filter(question_type= question_type)
    print(latest_question_list)
    question = Question.objects.filter(question_type= question_type)
    print("{} user name is".format(request.user.is_authenticated))
    context = {
        'latest_question_list': latest_question_list,
        'question': question
    }
    print(context)
    return render(request, 'polls/question_list.html', context)


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/result.html'


@login_required
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You dident select"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:detail', args=(question.id + 1,)))


def create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
        "question": question,
    }
    print(request.POST)
    choice_id = request.POST.get('asd')
    if request.method == "POST":
        if 'dodaj' in request.POST:
            print("dodaj")
            question.choice_set.create(choice_text=request.POST.get('new_choice'), votes=0)


        elif 'usun' in request.POST and 'asd' in request.POST:
            choice_id = request.POST.getlist('asd')
            for ids in choice_id:
                question.choice_set.get(id=ids).delete()
            print(choice_id)
            # print(question.choice_set.get(id= choice_id))
            # question.choice_set.get(id= choice_id).delete()
        return render(request, 'polls/create.html', context)


    else:
        print("Nie było POST")
        return render(request, 'polls/create.html', context)


def add(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
        "question": question,
    }
    return render(request, 'polls/index.html', context)

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     print(context)
#     return render(request, 'polls/index.html', context)
#
#
# def detail(request, question_id):
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist")
#     # return render(request, 'polls/detail.html', {'question':question})
#     question = get_object_or_404(Question, pk=question_id)
#     print(question)
#     return render(request, 'polls/detail.html', {'question': question})
#
#
# def results(request, question_id):
#     response = "You are looking at the result of question %s."
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/result.html', {
#         'responser': response,
#         'question': question
#     })
#
#
# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You dident select"
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
