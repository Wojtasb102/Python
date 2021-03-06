from django.urls import path
from . import views

app_name = "polls"
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:username>/category', views.category_list,name='category_list'),
    path('<str:username>/category', views.category_list,name='category_list_admin'),
    path('a/', views.user_list,name='user_list'),
    path('<str:category>/<str:username>/answer_list', views.answer_list,name='answer_list'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:question_id>/create/', views.create, name='create'),
    path('<int:question_id>/add/', views.create, name='add'),
    path('<str:question_type>/question_list/', views.QuestionList, name='question_list'),

]


# urlpatterns = [
#     # ex /polls/
#     path('', views.index, name='index'),
#     # ex /polls/5/
#     path('<int:question_id>/', views.detail, name='detail'),
#     # ex /polls/5/results/
#     path('<int:question_id>/results/', views.results, name='results'),
#     # ex /polls/5/vote/
#     path('<int:question_id>/vote', views.vote, name='vote'),
# ]
