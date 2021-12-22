from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# 21/12/10 조준모 게시판 모델 작성
# django 모델 : 데이터를 저장하기위해 생성하는 코드
#  -> DB의 테이블을 생성.
#  -> Django의 경우 ORM이라는것을 통해 테이블을 생성하고 수정, 삭제 할수 있음.
#  -> SQL문의 획일화(코드로 하기때문에)
#  -> DB가 변경되어도 쿼리를 변경할 이유가없다.

# 모델명(question)
# 속성명     설명
# subject  질문 제목(질문명)
# content  질문 내용
# create_date 질문 작성일시

class Question(models.Model):
    # null=true와 blank=true를 동시에 적용시킨 이유?
    # blank=true is.valid에서 빈값이어도 된다는 의미.
    # related_name : 속성의 정확한 명칭을 지정
    modify_date = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    voter = models.ManyToManyField(User, related_name='voter_question')

    def __str__(self):
        return self.subject
# 모델명 (Answer)
# 속성명        설명
# question     질문
# content      답변내용
# create_date  답변작성일

class Answer(models.Model):
    modify_date = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    voter = models.ManyToManyField(User, related_name='voter_answer')

#댓글 모델
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)

#12월 13일 퀴즈 정답
class Test(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_col = models.DateTimeField()