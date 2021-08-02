from django.contrib.auth.models import User
from django.db import models

# Create your models here.

# 나중엔 어떤 내용들어갈지 생각해본 후에 주도적으로 짜보기
class Article(models.Model):
    # OneToOneField : 객체 하나당 연결되는 거. 근데 우리는 1: 다 연결해야됨. user 한명이 게시글 여러개 작성할 수 있으니까ㅏ
    # 게시글 작성자가 탈퇴해도 게시글은 남아있게
    writer = models.ForeignKey(User, on_delete=models.SET_NULL,
                               related_name='article', null=True)
    # 게시글 작성할 때 받을 정보. CharField : 중단문
    title = models.CharField(max_length=200, null=True)
    # article 이라는 별도의 폴더가 생기고 그 안에 이미지가 쌓이도록
    image = models.ImageField(upload_to='article/', null=True)
    # TextField : 장문
    content = models.TextField(null=True)
    # 언제 작성했는지에 대한 시간정보 추가하기
    # auto_now_add : 값이 생성되는 순간 자동으로 설정되도록
    created_at = models.DateField(auto_now_add=True, null=True)