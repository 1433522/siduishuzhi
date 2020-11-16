from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse
from .models import Addr,Shuzhizhe

def index(request):
    # 未述职者随机进行述职: 如果你想进行随机排序,可以直接传入'?'即可。
    status0 = Shuzhizhe.objects.filter(status=0).order_by('?',)[:5]
    status1 = Shuzhizhe.objects.filter(status=1).order_by('?')[:5]
    status2 = Shuzhizhe.objects.filter(status=2).order_by('?')[:5]
    print(status0)

    # 所有人员按照营区排序
    status0fixed = Shuzhizhe.objects.filter(status=0).order_by("addr")
    status1fixed = Shuzhizhe.objects.filter(status=1).order_by("addr")
    status2fixed = Shuzhizhe.objects.filter(status=2).order_by("addr")

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
