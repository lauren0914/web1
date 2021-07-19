# UserCreationForm 안에 있는 password1, 2가 아이디, 비밀번호 바꾸는 거. 그래서 상속 받아서 커스텀을 하자
from django.contrib.auth.forms import UserCreationForm


class AccountCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        # super 메소드는 부모 메소드에 접근하기 위한 거
        # 이쪽은 이해해야됨
        # *args, **kwargs 선택적매개변수를 다 받아서 그대로 부모 메소드한테 넣어주는 거
        super().__init__(*args, **kwargs)
        # username 필드를 사용하지 않을 거야. 
        
        # 이해할 필요 없음
        self.fields['uesrname'].disabled = True
        