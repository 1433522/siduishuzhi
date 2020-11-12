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
    ordering = ('addr','name')
    list_display_links = ('name',)


