from django.shortcuts import render, get_object_or_404
from ..models import Question
from django.core.paginator import Paginator
from django.db.models import Q, Count

# 페이징
# 출력될 페이지의 데이터만 나눠서 가져오는것

# 페이징 객체 정리
# paginator.count : 전체 게시물 개수
# paginator.per_page : 페이지당 보여줄 게시물 개수
# paginator.page_range : 페이지 범위
# number : 현재 페이지 번호
# previous_page_number : 이전 페이지 번호
# next_page_number : 다음 페이지 번호
# has_previous : 이전 페이지 유무
# has_next : 다음 페이지 유무
# start_index : 현재 페이지 시작 인덱스
# end_index : 현재 페이지 끝 인덱스

# 페이징 기능 정리
# 이전페이지가 있는지 체크 : {% if question_list.has_previous %}
# 이전페이지 번호 : {{ question_list.previous_page_number }}
# 다음 페이지가 있는지 체크 : {% if question_list.has_next %}
# 다음페이지 번호 : {{ question_list.next_page_number }}
# 페이지 리스트 루프 {% for page_number in question_list.paginator.page_range %}
# 현재 페이지와 같은지 체크 {% if page_number == question_list.number %}

# 앵커
# url 호출시 원하는 위치로 이동시켜주는 태그.

# 앵커가 왜 필요하지?
#



def index(request):

    page = request.GET.get('page', '1') #페이징
    kw = request.GET.get('kw', '') # 검색어
    so = request.GET.get('so', 'recent')# 정렬기준

    # order_by() : 조회결과 정렬 / 속성 앞에 -가 붙으면 내림차순(역순)정렬
    # 정렬
    if so =='recent':
        question_list = Question.objects.order_by('-create_date')
    elif so =='recommend':
        question_list = Question.objects.annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    elif so == 'popular':
        question_list = Question.objects.annotate(num_answer=Count('answer')).order_by('-num_answer', '-create_date')

    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) | # subject 컬럼(속성)에 변수 kw에 저장된값이 포함됐는가?
            Q(content__icontains=kw) | # 내용검색
            Q(author__username__icontains=kw) | # 질문 작성자 검색
            Q(answer__author__username__icontains=kw)#답변 작성자 검색
        ).distinct()



    #페이징처리(한 페이지당 몇개씩 보여줄것인가?)
    paginator = Paginator(question_list, 5)
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj, 'page': page, 'kw': kw, 'so': so}
    #render : 파이썬 데이터를 템플릿에 적용해 HTML로 리턴하는 함수
    #         question_list라는 변수에 데이터를 담고 해당 html파일에 적용.
    return render(request, 'board/question_list.html', context)
# def error(request):
#     raise Http404("없ㅋ엉")

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'board/question_detail.html', context)

# 데코레이터 : 사전적의미로는 인테리어 디자이너의 의미를 가짐.
# 클로저와 비슷한 형태지만 함수를 파라미터로 받는 차이점이 있음


# view 함수
# 항상 request를 파라미터로 받아서 함수 실행에 대한 결과를
# response를 통해 처리

# 템플릿 태그
# 파이썬 코드와 HTML을 연결하기 위해 사용하는 태그
# 1. 분기
# {% if 조건문 %}
#    조건문에 해당하는 html코드
# {% elif 조건문 %}
#    조건문에 해당하는 html코드
# {% else 조건문%}
#    if도 elif도 해당하지 않는경우
# {% endif %}
# 2. 반복
# {% for item in list %}
#   내용{{ forloop.counter}}
# {% endfor %}
# forloop.counter : 루프 내의 순서로 1부터 표시
# forloop.counter(): 루프 내의 순서로 0부터 표시
# forloop.first : 첫번째 순서일경우 True
# forloop.last : 마지막 순서일경우 True
# 3. 객체
# {{ item }}
# {{ item.속성 }}

# HTTP 주요 응답코드
# 404 : not found (페이지를 찾을수 없음)
# 200 : 연결성공
# 500 : 서버에러