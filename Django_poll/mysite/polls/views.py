from django import template
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.urls import reverse
from django.views import generic

from .models import Question, Choice, Answer, Profile
from django.utils import timezone


# Create your views here.

def index(request):
    if request.user.is_superuser:
        return HttpResponseRedirect(reverse('polls:user_list'))
    else:
        return HttpResponseRedirect(reverse('polls:category_list', args={'username': request.user.username}))


def user_list(request):
    user_list = []
    for user in User.objects.all():
        if not user.is_superuser:
            user_list.append(user)
    context = {
        'users': user_list
    }

    return render(request, 'polls/user_list.html', context)


def category_list(request, username):
    if request.user.is_superuser:
        category_list = User.objects.get(username=username).profile.my_field
        context = {
            'category_list': category_list,
            'username': username,
        }
        return render(request, 'polls/category_list_admin.html', context)
        # return HttpResponseRedirect(reverse('polls:detail', args=(question.id + 1,)))
        # user_list=[]
        # print(User.objects.all())
        # for user in User.objects.all():
        #     print(user)
        #     if not user.is_superuser:
        #         user_list.append(user)
        # context = {
        #     'latest_question_list': user_list
        # }
    else:
        latest_question_list = User.objects.get(username=request.user.username).profile.my_field
        context = {
            'latest_question_list': latest_question_list,
        }
        return render(request, 'polls/category_list.html', context)


def answer_list(request, category, username):
    answer = []
    questions = Question.objects.filter(question_type=category)
    for q in questions:
        answer.append(q.question.filter(user=username).first())

    context = {
        'answers': answer
    }

    return render(request, 'polls/answer_list.html', context)

    # return User.objects.get(username="Wojciech").profile.my_field

    # # zwróć 5 ostatnich pytań
    # return Question.objects.filter(
    #     pub_date__lte=timezone.now()
    # ).order_by('-pub_date')[:5]


def QuestionList(request, question_type):
    latest_question_list = Question.objects.filter(question_type=question_type).order_by('question_number')
    question = Question.objects.filter(question_type=question_type)
    answer = []
    for q in question:
        if q.question.filter(user=request.user.username).exists():
            answer.append(q.question.filter(user=request.user.username).first().answer)
        else:
            answer.append("")
    context = {
        'latest_question_list': latest_question_list,
        'question': question,
        'answer': answer
    }
    return render(request, 'polls/question_list.html', context)


def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, 'polls/detail.html', {'question':question})
    q = get_object_or_404(Question, pk=question_id)
    answer = " "

    if q.question.filter(user=request.user.username).exists():
        answer = q.question.filter(user=request.user.username).first().answer
        print(q.question.filter(user=request.user.username).first().answer)

    return render(request, 'polls/detail.html', {'question': q, 'answer': answer})


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/result.html'


@login_required
def vote(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    # try:
    #     selected_choice = question.choice_set.get(pk=request.POST['choice'])
    # except (KeyError, Choice.DoesNotExist):
    #     return render(request, 'polls/detail.html', {
    #         'question': question,
    #         'error_message': "You dident select"
    #     })
    # else:
    username = request.user.username
    question_type = q.question_type
    print(q.answer_type)
    if q.answer_type == 'Wielokrotnego wyboru':
        answer = request.POST.getlist('choice')
    else:
        answer = request.POST.get('choice')
    a = q.question.filter(user=username)
    print(answer)
    if not a:
        print("lista pusta")
        q.question.create(user=username, answer=answer)
    else:
        print("lista pelna")
        a.update(answer=answer)

    return HttpResponseRedirect(reverse('polls:question_list', kwargs={"question_type":question_type}))


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
