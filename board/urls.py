from django.urls import path

from .views import base_views, question_views, answer_views, comment_views

# url 별칭의 사용이유?
# 별칭을 사용함으로써 url의 체계가 바뀌어도
# 템플릿단의 수정을 최소화 하기 위해.(자동수정)

app_name = 'board'

urlpatterns = [
    path('', base_views.index, name='index'),
    path('<int:question_id>/', base_views.detail, name='detail'),
    path('answer/create/<int:question_id>/', answer_views.answer_create, name='answer_create'),
    path('question/create/', question_views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/', question_views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/', question_views.question_delete, name='question_delete'),
    path('answer/modify/<int:answer_id>/', answer_views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/', answer_views.answer_delete, name='answer_delete'),
    path('comment/create/question/<int:question_id>', comment_views.comment_create_question, name='comment_create_question'),
    path('comment/modify/question/<int:comment_id>', comment_views.comment_modify_question, name='comment_modify_question'),
    path('comment/delete/question/<int:comment_id>', comment_views.comment_delete_question, name='comment_delete_question'),
    path('comment/create/answer/<int:answer_id>', comment_views.comment_create_answer, name='comment_create_answer'),
    path('comment/modify/answer/<int:comment_id>', comment_views.comment_modify_answer, name='comment_modify_answer'),
    path('comment/delete/answer/<int:comment_id>', comment_views.comment_delete_answer, name='comment_delete_answer'),
    #path('vote/question/<int:question_id>/', question_views.vote_question, name='vote_question'),
    path('vote/question/<int:question_id>/', question_views.vote_question, name='vote_question'),
    path('vote/answer/<int:question_id>/', answer_views.vote_answer, name='vote_answer'),
]