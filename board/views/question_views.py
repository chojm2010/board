from django.shortcuts import render, get_object_or_404, redirect
from ..models import Question
from django.utils import timezone
from ..forms import QuestionForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url='common:login')
def question_modify(request, question_id):

    question = get_object_or_404(Question, pk=question_id)
    # 권한체크
    # 글쓴 사람만 해당 글을 수정할수 있도록 체크.
    if question.author != request.user:
        messages.error(request, '수정권한이 없습니다.')
        return redirect('board:detail', question_id=question.id)

    if request.method =="POST":
        #request
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.modify_date = timezone.now()
            question.save()
            return redirect('board:detail', question_id=question.id)
    else:
        form = QuestionForm(instance=question)
    return render(request, 'board/question_form.html', {'form': form})

@login_required(login_url='common:login')
def question_create(request):

    # 권한체크
    # 글쓴 사람만 해당 글을 수정할수 있도록 체크.

    if request.method =="POST":
        #request
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.create_date = timezone.now()
            question.save()
            return redirect('board:index')
    else:
        form = QuestionForm()
    return render(request, 'board/question_form.html', {'form': form})

@login_required(login_url='common:login')
def question_delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    if question.author != request.user:
        messages.error(request, '삭제권한이 없습니다.')
        return redirect('board:detail', question_id=question.id)
    question.delete()
    return redirect('board:index')

@login_required(login_url='common:login')
def vote_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user == question.author:
        messages.error(request, '본인이 작성한 글을 추천할수 없습니다.')
    else:
        # Question 모델의 voter는 여러사람을 추가할수 있는 ManyToMany 이므로
        # add함수를 통한 처리가 필요하다.
        question.voter.add(request.user)
    return redirect('board:detail', question_id=question.id)