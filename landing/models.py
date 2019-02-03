'''
Модель - это описание полей в таблице базы данных
'''

from django.db import models


class Subscriber(models.Model):    #Название таблицы в базе данных
    email = models.EmailField()    #Тип поля имейл
    name = models.CharField(max_length=128)   #Тип поля текстовый, макс длина симолов 128
                                            #обязаьельный параметр макс длина
    def __str__(self):
        return "Пользователь %s %s" % (self.name, self.email)

    class Meta:
        verbose_name = 'MySubscriber'
        verbose_name_plural = 'A lot of Subcsribers'