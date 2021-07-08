from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from accountapp.models import HelloWorld


def hello_world(request):
    # return HttpResponse('Hello World!')
    if request.method == 'POST':
        temp = request.POST.get('input')

        new_data = HelloWorld()
        new_data.text = temp
        new_data.save()

        return render(request, 'accountapp/hello_world.html',
                      context={'new_data': new_data})
    else:
        return render(request, 'accountapp/hello_world.html',
                      context={'text': 'GET METHOD!'})

# request : 요청 관련 정보가 들어오는 곳. 지금은 안 씀
# template name