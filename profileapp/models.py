from email.mime import image

import nickname as nickname
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# models 안에 있는 Model 상속받기
class Profile(models.Model):
    # 안에 들어갈 속성 작성하기
    # 프로필, 계정 1대1로 연결해주기
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='profile')
    # db 연결, on_delete 속성에 models. 안에 있는 저거 넣어줄 거. 계정 삭제되면 어떤 행동을 취할 것이냐.
    # CASCADE : 종속. 계정이 삭제되면, 얘도 삭제된다. (SET.NULL 하면 연결된 객체가 삭제돼도 남아있음)

    # 이미지를 받는 필드
    image = models.ImageField(upload_to='profile/', null=True)
    nickname = models.CharField(max_length=30, unique=True, null=True) # 닉네임 겹치면 안 되니까
    message = models.CharField(max_length=200, null=True)
    # pillow : 파이썬 이미지 라이브러리. 설치 후에 makemigrations 하면 migraionts 폴더에 0001 에 변화 추적됨