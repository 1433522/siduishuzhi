from django import template
from ..models import Shuzhizhe

register = template.Library()

# 今天参加述职的人数
@register.simple_tag(name='total0')
def total0():
    return Shuzhizhe.objects.filter(status=0).count()


# 下次参加述职的人数
@register.simple_tag(name='total1')
def total1():
    return Shuzhizhe.objects.filter(status=1).count()

# 所有述职完毕的人数
@register.simple_tag(name='total2')
def total2():
    return Shuzhizhe.objects.filter(status=2).count()

