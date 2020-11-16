from django.contrib import admin
from .models import Addr,Shuzhizhe

# Register your models here.
@admin.register(Addr)
class AddrAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Shuzhizhe)
class ShuzhizheAdmin(admin.ModelAdmin):
    list_display = ('name','photo','addr','status')
    list_filter = ('addr','status')
    list_editable = ['addr','status']
    search_fields = ('name',)
    ordering = ('addr','status')
    list_display_links = ('name',)
    actions = ['changetostatus0','changetostatus1']

    # 添加admin动作（今天来述职）
    def changetostatus0(self,request,queryset):
        queryset.update(status=0)

    changetostatus0.short_description = "今天参加述职"

    # 添加admin动作（下次再来述职）
    def changetostatus1(self,request,queryset):
        queryset.update(status=1)

    changetostatus1.short_description = "下次再来述职"
