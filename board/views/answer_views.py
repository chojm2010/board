from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from ..models import Question, Answer
from django.utils import timezone
from ..forms import AnswerForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# resolve_url : 실제 호출되는 url문자열을 리턴하는 장고 함수

@login_required(login_url='common:login')
def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.author = request.user
            answer.save()
            return redirect('{}#answer_{}'.format(resolve_url('board:detail', question_id=question.id),answer.id))
    else:
        form = AnswerForm()
    return render(request, 'board/question_detail.html', {'question': question, 'form': form})
    #redirect : 페이지 이동을 위한 함수.
    #render와의 차이는 : redirect는 함수 자체를 다시 호출한다.

@login_required(login_url='common:login')
def answer_delete(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)

    if answer.author != request.user:
        messages.error(request, '삭제권한이 없습니다.')
    else:
        answer.delete()
    return redirect('board:detail', question_id=answer.question.id)

@login_required(login_url='common:login')
def answer_modify(request, answer_id):

    answer = get_object_or_404(Answer, pk=answer_id)
    # 권한체크
    # 글쓴 사람만 해당 글을 수정할수 있도록 체크.
    if answer.author != request.user:
        messages.error(request, '수정권한이 없습니다.')
        return redirect('{}#answer_{}'.format(resolve_url('board:detail', question_id=answer.question.id),answer.id))

    if request.method =="POST":
        #request
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.modify_date = timezone.now()
            answer.save()
            return redirect('board:detail', question_id=answer.question.id)
    else:
        form = AnswerForm(instance=answer)
    return render(request, 'board/answer_form.html', {'answer': answer, 'form': form})

@login_required(login_url='common:login')
def vote_answer(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user == answer.author:
        messages.error(request, '본인이 작성한 글을 추천할수 없습니다.')
    else:
        # Question 모델의 voter는 여러사람을 추가할수 있는 ManyToMany 이므로
        # add함수를 통한 처리가 필요하다.
        answer.voter.add(request.user)
    return redirect('board:detail', question_id=answer.question.id)