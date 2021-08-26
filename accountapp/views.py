from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User # 여기도 확인하기
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, \
    DeleteView  # 장고에서 view 안에 generic(중요함!)에서 Createview 를 가져왔다.
from django.views.generic.list import MultipleObjectMixin

from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountCreationForm
from accountapp.models import HelloWorld

# login url 어딨는지 알려주기
from articleapp.models import Article


#

# request : 요청 관련 정보가 들어오는 곳. 지금은 안 씀
# template name

# class based view!! 모든 CBV에서 crud 기능을 제공함. read 는 나중에 detail로 부를 거야(?)
# 계정(얘는 필수적이라(모든 사이트에서 거의 다 쓰는 기능이잖아.) 장고에서 기본적으로 제공해주는 디폴트 모델이 있음) 나중엔 우리가 만들겠지만.
class AccountCreateView(CreateView): # 상속
    # 무엇을 만들 것인지? user의 정보를 입력받을 모델을 만들고(?)
    # 이 변수명은 고정임. 이 cbv에서 제공하는 그대로
    # 무슨 모델을 사용할 것이냐? 장고에서 기본으로 제공하는 User 라는 모델을 사용. User에서 ctrl b 를 누르면 AbstractUser 를 상속받고 있고, 
    # 또 들어가보면, username, email 등 정보들 + 기본적인 검증데이터 등이 이미 설정된 상태로 제공이 된다. 이걸 상속받아서 열 추가할수도 있음
    model = User
    # user data를 넣을 입력 form
    form_class = UserCreationForm # 얘도 장고에서 제공해주는 거 있음
    # create 가 정상적으로 이뤄진 후에 어느 url로 연결할 것인가?
    success_url = reverse_lazy('articleapp:list')
    # reverse_lazy : 함수형에서는 reverse 썼는데 여기서는 lazy 왜 붙여요?
    # 함수에서 reverse 불러올 때는 바로 호출, class에서는 나중에 불러오기 때문에? lazy를 쓴다. 걍 외워
    # 함수와 클래스가 파이썬에서 불러와지는 방식의 차이
    template_name = 'accountapp/create.html' # 노란색으로 지금 html 파일이 없다고 뜸. 노란색은 파일이 없다는 걸 알려주는 거구나 ㅇㅅㅇ


    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.pk})


class AccountDetailView(DetailView, MultipleObjectMixin):
    # 어떤 모델의 상세정보를 볼 건지. 모델 지정해주기. 위에서 사용한 모델
    model = User
    # 특정 account 객체의 이름을 뭐라고 정할 것이냐. 이름 지어주기? 나중에 템플릿에서 사용하기 위해서
    context_object_name = 'target_user'
    # html 뭐 쓸 건지
    template_name = 'accountapp/detail.html'
    # 라우팅 : 어떤 url로 들어가야 이 로직이 작동될 건지.

    paginate_by = 20

    def get_context_data(self, **kwargs):
        article_list = Article.objects.filter(writer=self.object)
        return super().get_context_data(object_list=article_list,
                                        **kwargs)

has_ownership = [login_required, account_ownership_required]
# 적용하고자 하는 모든 데코레이터를 리스트 안에 넣을 거야.

# 데코레이터는 함수에 쓰는 애야. 그래서 클래스를 함수로 바꿔주는 데코레이터 있음!
# get 방식의 http 에 적용해주겠다 명시..?
# @method_decorator(login_required, 'get')
# @method_decorator(login_required, 'post')
@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    # 어떤 것을 수정할 것인지 모델 적기
    model = User
    # 수정할 수 있는 입력 form이 있어야됨(장고애서 기본으로 제공해주는)
    # UserCreationForm 안에 있는 password1, 2가 아이디, 비밀번호 바꾸는 거?? 그래서 상속 받아서 커스텀을 하자
    form_class = AccountCreationForm
    context_object_name = 'target_user'
    template_name = 'accountapp/update.html'

    # 얘는 클래스 안에 있는 메소드이기 때문에 데코레이터가 바로 안 먹음.
    # def get(self, request, *args, **kwargs):
    #     if request.user.is_authenticated and self.get_object() == request.user:
    #         return super().get(request, *args, **kwargs)
    #     else:
    #         return HttpResponseForbidden()
    #
    # def post(self, request, *args, **kwargs):
    #     if request.user.is_authenticated and self.get_object() == request.user:
    #         return super().post(request, *args, **kwargs)
    #     else:
    #         return HttpResponseForbidden()
    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk':self.object.pk})

# 탈퇴(form 필요없이)
@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    # 이 이름을 통해서 객체에 접근하겠다
    context_object_name = 'target_user'
    success_url = reverse_lazy('articleapp:list')
    # delete 안에 있는 로직 알 필요 없음!! 작성할 필요 없음! 안에 들어있으니까.
    template_name = 'accountapp/delete.html'



    # def get(self, request, *args, **kwargs):
    #     # and : 이 user가 해당 페이지 주인이 맞는지 확인. self.get_object() self는 저 view 자체를 의미 -> target user를 가져오기
    #     if request.user.is_authenticated and self.get_object() == request.user:
    #         return super().get(request, *args, **kwargs)
    #     else:
    #         return HttpResponseForbidden()
    #
    #     def post(self, request, *args, **kwargs):
    #         if request.user.is_authenticated and self.get_object() == request.user:
    #             return super().post(request, *args, **kwargs)  # 부모 메소드에서 pos 불러오기
    #         else:
    #             return HttpResponseForbidden()




