from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from articleapp.forms import ArticleCreationForm
from articleapp.models import Article


class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'articleapp/create.html'

    # ????? 뭐가 문제? 
    def form_valid(self, form):
        # 검증 완료된 form의 instance에 접근해서 user를 wirter 에 할당
        form.instance.writer = self.request.user
        return super().form_valid(form)