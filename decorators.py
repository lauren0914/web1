
# 인자로 함수를 받음. 함수 내에서 새로운 함수 만들기
# 여기서 들어가는 func이 hello_world가 되는 거
def decorator(func):
    def decorated(input_text):
        print('함수 시작!')
        func(input_text)
        print('함수 끝!')
    return decorated
    # 호출 아니고 리턴!

@decorator
def hello_world(input_text):
    print(input_text)

hello_world('Hello World!')


# def decorator(func):
#     if func.h < 0 and func.v < 0:
#         print('error')
#     else:
#         def Square(h, v):
#             area = h * v
#             print(area)
#
#         def triangle(h, v):
#             area = h * v * 0.5
#             print(area)
#
# @decorator
# def get_area(h, v):
#     return h, v
#
# get_area(5, 10)

def check_integer(func):
    def decorated(width, height):
        if width >= 0 and height >= 0:
            return func(width, height)
        else:
            raise ValueError
    return decorated

@check_integer
def rect_area(width, height):
    return width * height

@check_integer
def tri_area(width, height):
    return width * height / 2

r_area = rect_area(-10, 10)
print(r_area)

t_area = tri_area(-10, 10)
print(t_area)



