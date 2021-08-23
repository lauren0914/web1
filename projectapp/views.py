from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.list import MultipleObjectMixin

from articleapp.models import Article
from projectapp.forms import ProjectCreationForm
from projectapp.models import Project
from subscribeapp.models import Subscription


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreationForm
    template_name = 'projectapp/create.html'

    def get_success_url(self):
        return reverse('projectapp:detail', kwargs={'pk' : self.object.pk})

# MultipleObjectMixin : ListView 역할 모방..? 여러 개의 객체들을 list로 보여준다.
class ProjectDetailView(DetailView, MultipleObjectMixin):
    model = Project
    context_object_name = 'target_project'
    template_name = 'projectapp/detail.html'

    paginate_by = 20

    # 템플릿에서 사용할 수 있도록 필터링..?
    # 템플릿에서 사용하는 문맥 데이터를 만들어주기 위한 메소드임. -> 구독여부 확인하는 로직 넣어주기
    def get_context_data(self, **kwargs):
        user = self.request.user
        # target_project랑 동일
        project = self.object

        # user가 로그인 되어있는지 확인. 원래 method ~ 하지 않았나요?
        # 그렇게 되면 문제가. 로그인 된 유저만 게시글을 볼 수 있잖아. 우리는 로그인 안 된 사람도 게시글 볼 수 있게 만들자
        if user.is_authenticated:
            subscription = Subscription.objects.filter(user=user,
                                                       project=project)
        else:
            subscription = None
        # -> subscription 에 구독여부를 확인할 수 있는 데이터가 들어있을 거야

        # 조건에 맞는 애들만 필터링하겠다. self.object = target_project
        article_list = Article.objects.filter(project=self.object)
        return super().get_context_data(object_list=article_list,
                                        subscription=subscription,
                                        **kwargs)


class ProjectListView(ListView):
    model = Project
    # 단일 객체가 아닌 여러 객체를 받아야됨. 아래 이름으로 만들어주기
    context_object_name = 'project_list'
    template_name = 'projectapp/list.html'
    paginate_by = 20