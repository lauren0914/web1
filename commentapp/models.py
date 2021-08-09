from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from articleapp.models import Article


class Comment(models.Model):
    # on_delete : 삭제정책. -> 지우지는 않고 null인 상태로 두겠다
    # 게시글, 댓글 연결하기
    article = models.ForeignKey(Article, on_delete=models.SET_NULL,
                                related_name='comment', null=True)
    writer = models.ForeignKey(User, on_delete=models.SET_NULL,
                               related_name='comment', null=True)
    # 클라이언트한테 댓글내용 입력받아야됨
    content = models.TextField(null=False)

    created_at = models.DateTimeField(auto_now_add=True)
