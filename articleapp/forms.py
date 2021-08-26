from django import forms
from django.forms import ModelForm

from articleapp.models import Article


class ArticleCreationForm(ModelForm):
    # 많은 것 중에 from django import forms 를 가져옴
    # 미디어에디터로 사용하기 위해 커스터마이징(detail에서 html 적용 안 된 상태로 나옴)
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable',
                                                           'style': 'min-height: 10rem;'
                                                                    'text-align: left;'}))
    class Meta:
        model = Article
        # 클라이언트로부터 어떤 데이터를 받아올 건지 적어주기
        # 모델에 추가한 project 속성 추가로 더 받음 -> 사이트 내에서 탭이 하나 더 생김.
        # 어떤 게시판에 글을 쓸지 선택할 수 있는 탭이 생김 ! 근데 각가 어떤 게시판인지 모름. 차이 만들어주기
        fields = ['title', 'image', 'content', 'project']

