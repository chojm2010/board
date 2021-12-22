from django import forms
from board.models import Question, Answer, Comment
# 폼
# 페이지 요청시 전달되는 파라미터들을 쉽게 관리하기위해 사용하는 클래스
# 필수 파라미터의 값이 누락되지 않았는지 형식은 적절한지 등을 검증할 목적으로 사용
# html을 자동으로 생성하거나 폼에 연결된 모델을 이용해 데이터를 저장할수도 있음.

# 장고의 폼 종류
# 일반폼
# 모델폼 : 모델과 연결된 폼, 폼 저장시 연결된 모델의 데이터를 저장할수 있는폼.
#         모델폼의 경우. Meta라는 클래스가 반드시 필요하다.

# 파이썬에서 클래스는 객체인가 아닌가 o, x
# 메타 클래스 : 클래스를 만드는 또다른 클래스.
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content']
        # widgets = {
        #     'subject': forms.TextInput(attrs={'class': 'form-control'}),
        #     'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 15}),
        # }
        labels = {
            'subject' : '제목',
            'content' : '내용',
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content' : '답변내용',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content' : '댓글내용',
        }
