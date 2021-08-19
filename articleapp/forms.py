from django.forms import ModelForm

from articleapp.models import Article


class ArticleCreationForm(ModelForm):
    class Meta:
        model = Article
        # 클라이언트로부터 어떤 데이터를 받아올 건지 적어주기
        # 모델에 추가한 project 속성 추가로 더 받음 -> 사이트 내에서 탭이 하나 더 생김.
        # 어떤 게시판에 글을 쓸지 선택할 수 있는 탭이 생김 ! 근데 각가 어떤 게시판인지 모름. 차이 만들어주기
        fields = ['title', 'image', 'content', 'project']