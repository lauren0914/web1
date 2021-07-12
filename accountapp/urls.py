from django.urls import path

from accountapp.views import hello_world, AccountCreateView

app_name = 'accountapp' # 라우팅 편리하게 하기 위해서 작성해둔 것

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),

    # AccountCreate class 이 진행될 url. r근데 hello_world 는 함수잖아.얘도 함수로 바꿔줘야됨(as_view())
    path('create/', AccountCreateView.as_view(), name='create') # / 주소를 안 쓰고 accountapp에 있는 create로 이동하라고 알려주려고 이름 정해두기
]
