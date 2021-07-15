from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User # 여기도 확인하기
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView  # 장고에서 view 안에 generic(중요함!)에서 Createview 를 가져왔다.

from accountapp.models import HelloWorld


def hello_world(request):
    # return HttpResponse('Hello World!')
    if request.method == 'POST':
        temp = request.POST.get('input')

        new_data = HelloWorld()
        new_data.text = temp # 이렇게 중단점을 만들어 줄 수 있음. 일반적인 runserver 에서는 안 먹히고. 오른쪽 상단에 debug라는 버튼을 누르면 중단점에서 멈추게 할 수 있음
        # 디버그 창(어디서 확인해?) 열어서 어떤 상태인지 알 수 있음. 어디서 에러났는지 확인할 수 있음. f8을 누르면 한줄한줄 넘어가는 걸 볼 수 있음.
        new_data.save() # save 함수 내부에서 어떤 일이 벌어나는지 알고 싶다. f7을 누르게 되면 save 함수로 들어갈 수 있음.
        # 들어가서 f8 누르면 내가 보고 있는 라인 기준으로 한줄한줄 실행시키는 것
        # f9를 누르게 되면, 다음 중단점까지 건너뛴다.
        
        # post 요청을 get 요청으로 redirect(재연결하는) 해준다. 새로고침할 때 마지막 요청(우리 사이트에서는 post요청이었음)을 반복하는 문제를 해결하기 위해서
        # 어디로 보낼 건지 알려줄 건데. / 기반의 주소로 안 쓸 거야. account 앱 안에 있는 hello_world(url name) 라우트로 보내라.
        # 근데 이렇게 하면 실행이 안 됨. 왜냐면 여기는 / 주소가 들어가야되거든. 그래서 / 주소로 역 변환을 해줄 거야(reverse)
        return HttpResponseRedirect(reverse('accountapp:hello_world'))
        
    else:
        # HelloWorld.objects : HelloWorld(데이터베이스)의 모든 객체를 가져온다
        data_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html',
                      context={'data_list': data_list})

# request : 요청 관련 정보가 들어오는 곳. 지금은 안 씀
# template name

# class based view!! 모든 CBV에서 crud 기능을 제공함. read 는 나중에 detail로 부를 거야(?)
# 계정(얘는 필수적이라(모든 사이트에서 거의 다 쓰는 기능이잖아.) 장고에서 기본적으로 제공해주는 디폴트 모델이 있음) 나중엔 우리가 만들겠지만.
class AccountCreateView(CreateView): # 상속
    # 무엇을 만들 것인지? user의 정보를 입력받을 모델을 만들고(?)
    # 이 변수명은 고정임. 이 cbv에서 제공하는 그대로
    model = User
    # user data를 넣을 입력 form
    form_class = UserCreationForm # 얘도 장고에서 제공해주는 거 있음
    # create 가 정상적으로 이뤄진 후에 넘어갈 url
    success_url = reverse_lazy('accountapp:hello_world') 
    # reverse_lazy : 위에서는 reverse 썼는데 여기서는 lazy 왜 붙여요? 함수에서 reverse 불러올 때는 바로 호출, class에서는 나중에 불러오기 때문에? lazy를 쓴다. 걍 외워
    template_name = 'accountapp/create.html' # 노란색으로 지금 html 파일이 없다고 뜸. 노란색은 파일이 없다는 걸 알려주는 거구나 ㅇㅅㅇ

class AccountDetailView(DetailView):
    # 어떤 모델의 상세정보를 볼 건지. 모델 지정해주기. 위에서 사용한 모델
    model = User
    # 특정 account 객체의 이름을 뭐라고 정할 것이냐. 이름 지어주기? 나중에 템플릿에서 사용하기 위해서
    context_object_name = 'target_user'
    # html 뭐 쓸 건지
    template_name = 'accountapp/detail.html'
    # 라우팅 : 어떤 url로 들어가야 이 로직이 작동될 건지.