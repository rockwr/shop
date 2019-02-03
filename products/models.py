'''
Модель - это описание полей в таблице базы данных
'''

from django.db import models


class Product(models.Model):    # Модель товара
    name = models.CharField(max_length=64, blank=True, null=True, default=None)   # Название товара
    description = models.TextField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False) #для даты, чтобы сохранялась дата,
    updated = models.DateTimeField(auto_now_add=False, auto_now=True) #когда заказали

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


# Модель товара, здесь будет только картинка длч данного товара
class ProductImage(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE)   # Ссылка на товар
    image = models.ImageField(upload_to='products_images/')
    is_active = models.BooleanField(default=True)  # для отображения объекта(картинки), можно отключить(False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False) #для даты, чтобы сохранялась дата,
    updated = models.DateTimeField(auto_now_add=False, auto_now=True) #когда заказали

    def __str__(self):
        return "Заказ %s" % self.id

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'