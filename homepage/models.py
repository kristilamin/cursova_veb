# Create your models here.
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    """Продукт"""

    class Meta:
        db_table = "product"
        verbose_name = "Продукт"
        verbose_name_plural = "Продукти"

    product_name = models.TextField(verbose_name="Назва продукту")
    wine_type = models.TextField(verbose_name="Тип")
    quantity_on_plant = models.IntegerField(verbose_name="Кількість на заводі")
    created_at = models.DateTimeField(verbose_name="Дата виготовлення", auto_now_add=True)
    price = models.IntegerField(verbose_name="Ціна (грн)")
    price_for_all = models.IntegerField(verbose_name="Ціна за всі одиниці продукту (грн)")
    surovuna_id = models.ForeignKey("Surovuna", on_delete=models.CASCADE, verbose_name="Ідентифікатор сировини")

    def __str__(self):
        return f"{self.product_name}"


# class Customer(models.Model):
#     """Покупець (власник винного магазину)"""

#     class Meta:
#         db_table = "customer"
#         verbose_name = "Дані про замовника"
#         verbose_name_plural = "Дані про замовників"

#     customer_name = models.TextField(verbose_name="Ім'я замовника")
#     phone = models.TextField(verbose_name="Номер телефону")
#     email = models.TextField(verbose_name="Електронна пошта")
#     # password = models.TextField(verbose_name="Пароль")
#     city = models.TextField(verbose_name="Місто замовника")
#     new_post_number = models.TextField(verbose_name="Номер відділення нової пошти")

#     def __str__(self):
#         return self.customer_name



class Surovuna(models.Model):
    """Сировина"""

    class Meta:
        db_table = "surovuna"
        verbose_name = "Сировина"
        verbose_name_plural = "Сировина"


    surovuna_name = models.TextField(verbose_name="Назва сировини")
    quantity_on_plant = models.IntegerField(verbose_name="Кількість сировини на заводі (тонн)")
    vurobnucha_price_kg = models.IntegerField(verbose_name="Ціна за кілограм сировини (грн)")
    vurobnucha_price_general_kg = models.IntegerField(verbose_name="Загальна ціна за сировину (грн)")
    delivery_price = models.IntegerField(verbose_name="Ціна доставки (грн)")
    delivery_name = models.TextField(verbose_name="Постачальник")


    def __str__(self):
        return f"{self.surovuna_name}"


STATUS_CHOICES = [
        ("Відкрито", "Відкрито"),
        ("Закрито", "Закрито"),
        ("В роботі", "В роботі"),
        ("Потребує уточнення", "Потребує уточнення"),
    ]

class Order(models.Model):
    """Замовлення"""

    class Meta:
        db_table = "order"
        verbose_name = "Замовлення"
        verbose_name_plural = "Замовлення"

    user_id = models.ForeignKey(User, verbose_name="Замовник", on_delete=models.CASCADE, default=1)
    product_id = models.ForeignKey(Product, verbose_name="Продукт", on_delete=models.CASCADE)
    quantity_of_product = models.IntegerField(verbose_name="Кількість продукту")
    created_at = models.DateTimeField(verbose_name="Дата замовлення", auto_now_add=True)
    last_updated_at = models.DateTimeField(verbose_name="Востаннє змінено", blank=True, null=True)
    order_status = models.CharField(max_length=20, verbose_name="Статус замовлення", choices=STATUS_CHOICES, default="open")


    def save(self, *args, **kwargs):
        self.last_updated_at = datetime.now()
        super().save(*args, **kwargs)