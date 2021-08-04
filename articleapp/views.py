from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from articleapp.forms import ArticleCreationForm
from articleapp.models import Article


class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'articleapp/create.html'

    # ????? 뭐가 문제? writer id 가 자동생성이 안 된다고?
    def form_valid(self, form):
        # 검증 완료된 form의 instance에 접근해서 user를 wirter 에 할당
        form.instance.writer = self.request.user
        return super().form_valid(form)

class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'target_article'
    template_name = 'articleapp/detail.html'