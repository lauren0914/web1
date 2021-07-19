from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import hello_world, AccountCreateView, AccountDetailView, AccountUpdateView

app_name = 'accountapp' # 라우팅 편리하게 하기 위해서 작성해둔 것

# 라우팅
urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),

    path('login/', LoginView.as_view(template_name='accountapp/login.html'),
         name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # AccountCreate class 이 진행될 url. 근데 hello_world 는 함수잖아.얘도 함수로 바꿔줘야됨(as_view())
    path('create/', AccountCreateView.as_view(), name='create'), # / 주소를 안 쓰고 accountapp에 있는 create로 이동하라고 알려주려고 이름 정해두기
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),
    # 이렇게만 쓰면 구동이 안됨. pk라는 게 없다! 프라이머리 키가 없다고! 어떤 객체ㅏ 가지고 있는 고유값.
    # 그걸 이 url 에 함께 포함시켜줘야 됨. 당연함. 어떤 디태일 값을 볼건지 고유값을 넘겨줘야지. account 가 하나만 있는 게 아니잖아.
#     <int:pk> : pk라는 이름의 숫자를 이 주소창에서 받을 거다
    # 얘도. 어떤 객체를 수정할 것인지 pk를 같이 보내줘야됨
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', AccountDetailView.as_view(), name='delete')
]
