from django.urls import path

from projectapp.views import ProjectCreateView

app_name = 'projectapp'
# revsere('projectapp:create') 이런 거 하려면.

urlpatterns = [
    path('create/', ProjectCreateView.as_view(), name='create'),

]