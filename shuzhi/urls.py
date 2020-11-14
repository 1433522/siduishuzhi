from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),#所有未述职人员
    path('show-<int:sid>', views.show, name='show'),#述职者个人
]

