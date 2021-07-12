from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from accountapp.models import HelloWorld


def hello_world(request):
    # return HttpResponse('Hello World!')
    if request.method == 'POST':
        temp = request.POST.get('input')

        new_data = HelloWorld()
        new_data.text = temp
        new_data.save()
        
        # post 요청을 get 요청으로 redirect(재연결하는) 해준다. 새로고침할 때 마지막 요청을 반복하는 문제를 해결하기 위해서
        # 어디로 보낼 건지 알려줄 건데. / 기반의 주소로 안 쓸 거야. account 앱 안에 있는 hello_world(url name) 라우트로 보내라.
        # 근데 이렇게 하면 실행이 안 됨. 왜냐면 여기는 / 주소가 들어가야되거든. 그래서 / 주소로 역 변환을 해줄 거야(reverse)
        return HttpResponseRedirect(reverse('accountapp:hello_world'))
        # HelloWorld.objects : HelloWorld 의 모든 객체를 가져온다
    else:
        data_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html',
                      context={'data_list': data_list})

# request : 요청 관련 정보가 들어오는 곳. 지금은 안 씀
# template name