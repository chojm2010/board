from django.shortcuts import render, get_object_or_404, redirect
from ..models import Question, Comment
from django.utils import timezone
from ..forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url='common:login')
def comment_create_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.create_date = timezone.now()
            comment.question = question
            comment.save()
            return redirect('board:detail', question_id=question.id)
    else:
        form = CommentForm()
    context = {'form': form}
    return render(request, 'board/comment_form.html', context)

@login_required(login_url='common:login')
def comment_modify_question(request, comment_id):

    comment = get_object_or_404(Comment, pk=comment_id)
    # 권한체크
    # 글쓴 사람만 해당 글을 수정할수 있도록 체크.
    if comment.author != request.user:
        messages.error(request, '수정권한이 없습니다.')
        return redirect('board:detail', question_id=comment.question.id)

    if request.method =="POST":
        #request
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('board:detail', question_id=comment.question.id)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'board/comment_form.html', {'comment': comment, 'form': form})

@login_required(login_url='common:login')
def comment_delete_question(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author != request.user:
        messages.error(request, '삭제권한이 없습니다.')
        return redirect('board:detail', question_id=comment.question.id)
    else:
        comment.delete()
    return redirect('board:detail', question_id=comment.question.id)


@login_required(login_url='common:login')
def comment_create_answer(request, answer_id):
    answer = get_object_or_404(Question, pk=answer_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.create_date = timezone.now()
            comment.answer = answer
            comment.save()
            return redirect('board:detail', question_id=comment.answer.question.id)
    else:
        form = CommentForm()
    context = {'form': form}
    return render(request, 'board/comment_form.html', context)

@login_required(login_url='common:login')
def comment_modify_answer(request, comment_id):

    comment = get_object_or_404(Comment, pk=comment_id)
    # 권한체크
    # 글쓴 사람만 해당 글을 수정할수 있도록 체크.
    if comment.author != request.user:
        messages.error(request, '수정권한이 없습니다.')
        return redirect('board:detail', question_id=comment.answer.question.id)

    if request.method =="POST":
        #request
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('board:detail', question_id=comment.answer.question.id)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'board/comment_form.html', {'comment': comment, 'form': form})

@login_required(login_url='common:login')
def comment_delete_answer(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author != request.user:
        messages.error(request, '삭제권한이 없습니다.')
        return redirect('board:detail', question_id=comment.answer.question.id)
    else:
        comment.delete()
    return redirect('board:detail', question_id=comment.answer.question.id)