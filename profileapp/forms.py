from django.forms import ModelForm

from profileapp.models import Profile


class ProfileCreationForm(ModelForm):
    # meta : 이미지에서 픽셀이 데이터임. 그 외적으로 사진을 표현하고 있는 데이터가 메타데이터임. 사진의 크기가 얼마인지, 언제 찍은 건지.등
    # 그 외부적인 데이터를 적어주는 거
    class Meta:
        # 우리가 만든 profile
        model = Profile
        # user한테서 뭐 받을 건지 정해주기
        fields = ['image', 'nickname', 'message']