from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView

# 좋아요 누르고 다시 페이지로 돌아가야하니까
from articleapp.models import Article
from likeapp.models import LikeRecord

@method_decorator(login_required, 'get')
class LikeArticleView(RedirectView):

    def get(self, request, *args, **kwargs):
        # 어떤 user가 요청을 보냈는지, 어떤 게시글에 좋아요를 눌렀는지
        user = request.user
        article = Article.objects.get(pk=kwargs['article_pk'])

        likeRecord = LikeRecord.objects.filter(user=user,
                                               article=article)
        # 좋아요 찍은 기록 있으면 저 페이지로 연결
        if likeRecord.exists():
            # 좋아요 반영 X
            # django.contrib
            #                     request, messages level, 보여줄 문구
            messages.add_message(request, messages.ERROR, '좋아요는 한 번만 가능합니다.')
            return HttpResponseRedirect(reverse('articleapp:detail', kwargs={'pk' : kwargs['article_pk']}))
        else:
            LikeRecord(user=user, article=article).save()
            article.like += 1
            # 실제 DB에 반영
            article.save()
            # 좋아요 반영 O
            messages.add_message(request, messages.SUCCESS, '좋아요가 반영되었습니다')


        return super().get(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        return reverse('articleapp:detail', kwargs={'pk' : kwargs['article_pk']})