from django.http import HttpResponseForbidden

from articleapp.models import Article


def article_ownership_required(func):
    def decorated(request, *args, **kwargs):
        # 요청 보낸 user와 게시물 작성자 확인
        # 특정 한개(주소창에 있던 pk값을 가지고 있는)의 article 객체 받아오기
        target_article = Article.objects.get(pk=kwargs['pk'])
        if target_article.writer == request.user:
            return func(request, *args, **kwargs)
        else:
            # 금지된 곳에 접근했다는 response 돌려주기
            return HttpResponseForbidden()
    return decorated