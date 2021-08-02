from django.forms import ModelForm

from articleapp.models import Article


class ArticleCreationForm(ModelForm):
    class Meta:
        model = Article
        # 클라이언트로부터 어떤 데이터를 받아올 건지 적어주기
        fields = ['title', 'image', 'content']