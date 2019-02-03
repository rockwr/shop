'''
Модель - это описание полей в таблице базы данных
'''

from django.db import models
from products.models import Product

class Status(models.Model):
    name = models.CharField(max_length=24, blank=True, null=True, default=None)  # указывать длину ближе к реальным цифрам
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False) #для даты, чтобы сохранялась дата,
    updated = models.DateTimeField(auto_now_add=False, auto_now=True) #когда заказали

    def __str__(self):
        return "Статус %s" % self.name

    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказа'


class Order(models.Model):    #Название таблицы в базе данных
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0) #total amounts for all products in order
    customer_email = models.EmailField(blank=True, null=True, default=None)    #Тип поля имейл
    customer_name = models.CharField(max_length=64, blank=True, null=True, default=None)   #Тип поля текстовый, макс длина симолов 128
    customer_phone = models.CharField(max_length=48, blank=True, null=True, default=None) #обязаьельный параметр макс длина
    customer_adress = models.CharField(max_length=128, blank=True, null=True, default=None)
    comments = models.TextField(blank=True, null=True, default=None)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, auto_now=False) #для даты, чтобы сохранялась дата,
    updated = models.DateTimeField(auto_now_add=False, auto_now=True) #когда заказали

    def __str__(self):
        return "Заказ %s %s" % (self.id, self.status.name)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class ProductsInOrder(models.Model):    #Название таблицы в базе данных
    order = models.ForeignKey(Order, blank=True, null=True, default=None, on_delete=models.CASCADE) #Ссылка на заказ;
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE)  #Ссылка на продукт
    nmb = models.IntegerField(default=1)   #количество
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0) #цена за 1 кол-во
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0) # Общая цена; цена+количесвто
    is_active = models.BooleanField(default=True) # Товар в заказе может быть отменен
    created = models.DateTimeField(auto_now_add=True, auto_now=False) #для даты, чтобы сохранялась дата,
    updated = models.DateTimeField(auto_now_add=False, auto_now=True) #когда заказали

    def __str__(self):
        return "%s" % self.product.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'