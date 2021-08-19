from django.db import models

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=20, null=False)
    # null은 입력하고 말고를 정하는 게 아니야. (그건 blank.) 서버에 null을 허용하느냐 마냐의 문제임
    description = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='project/', null=False)

    created_at = models.DateTimeField(auto_now_add=True)
    
    # 내부 스페셜 메소드. 인스턴스가 출력되거나, 문자열을 되돌려줘야할 때 어떤 값을 되돌려 줄 건지 선택하는 거
    def __str__(self):
        # 게시판 이름
        return self.name