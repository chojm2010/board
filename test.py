# def outer_func(msg):
#     def inner_func():
#         print(msg)
#     return inner_func
#
# hello_func = outer_func('hi')
#
# hello_func()

def login_required(func):
    def wrapper_function():
        print('{} 함수가 호출되기전 입니다.'.format(original_function.__name__))
        return original_function()

    return wrapper_function
@login_required
def question_create():
    print('display_1 함수가 실행됐습니다.')
@login_required
def answer_create():
    print('display_2 함수가 실행됐습니다.')

# display_1 = decorator_function(display_1)  # 1
# display_2 = decorator_function(display_2)  # 2

question_create()
print()
answer_create()
