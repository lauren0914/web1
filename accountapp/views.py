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

        # HelloWorld.objects : HelloWorld 의 모든 객체를 가져온다
        data_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html',
                      context={'data_list': data_list})
    else:
        data_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html',
                      context={'data_list': data_list})

# request : 요청 관련 정보가 들어오는 곳. 지금은 안 씀
# template name