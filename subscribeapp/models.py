from django.contrib.auth.models import User
from django.db import models

# Create your models here.

# user 와 project 연결
from projectapp.models import Project


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='subscription', null=False)
    # 구독정보가 연결되어있는 유저가 사라지면 구독정보도 사라진다.
    # 어떤 user가 어떤 게시판을 구독했는지에 대한 정보니까. 비어있으면 안됨
    project = models.ForeignKey(Project, on_delete=models.CASCADE ,
                                related_name='subscription', null=False)
    # user는 게시판당 구독 하나만 가능
    # meta = 외부정보. 필드가 아닌 모든 정보를 메타 정보라고 함. unique_together : 메타 옵션
    class Meta:
        unique_together = ['user', 'project']