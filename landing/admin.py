from django.contrib import admin
from .models import *

class SubscriberAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Subscriber._meta.fields] #отобразить все поля
    #exclude = ["email"] #не отображать выбранное поле
    #fields = ["email"]  #противоположное exclude, только то, что мы показываем
    list_filter = ['name']  #фильтр по выбранному полю
    search_fields = ['name', 'email']


    class Meta:
        model = Subscriber


admin.site.register(Subscriber, SubscriberAdmin)
