from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello_world(request):
    # return HttpResponse('Hello World!')
    if request.method == 'POST':
        return render(request, 'accountapp/hello_world.html',
                      context={'text': 'POST METHOD!'})
    else:
        return render(request, 'accountapp/hello_world.html',
                      context={'text': 'GET METHOD!'})

# request : 요청 관련 정보가 들어오는 곳. 지금은 안 씀
# template name