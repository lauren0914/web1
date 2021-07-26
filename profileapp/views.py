from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/create.html'

    # 오버라이드
    def form_valid(self, form):
        # form(위ㅇ의 ProfileCreationForm을 말하는 거)에 부족한 user 를 넣어준다 근데 form에 3개밖에 없어서 못 넣어줌. -> 그냥 user가 아니라 instance.user
        form.instance.user = self.request.user
        return super().form_valid(form)