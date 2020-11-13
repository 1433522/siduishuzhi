from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse
from .models import Addr,Shuzhizhe

def index(request):
    # 未述职者随机进行述职: 如果你想进行随机排序,可以直接传入'?'即可。
    status0 = Shuzhizhe.objects.filter(status=0).order_by('?',)[:8]
    # 下次述职和述职完毕的人按照营区排序
    status1 = Shuzhizhe.objects.filter(status=1).order_by('?')[:8]
    status2 = Shuzhizhe.objects.filter(status=2).order_by('?')[:8]
    print("status0:"+str(status0))
    print("status1:"+str(status1))
    print("status2:"+str(status2))

    return render(request,
            'shuzhi/index.html',
            locals())

def show(request,sid):
    shuzhizhe = get_object_or_404(Shuzhizhe,pk=sid)
    shuzhizhe.status = 2
    shuzhizhe.save()
    nextone = None
    if Shuzhizhe.objects.filter(status=0):
        nextone = Shuzhizhe.objects.filter(status=0)[0]
    return render(request,
            'shuzhi/show.html',
            locals())

def done(request,did):
    shuzhizhe = get_object_or_404(Shuzhizhe,pk=did)
    shuzhizhe.status = 2
    shuzhizhe.save()
    return redirect('http://127.0.0.1:8000/')
