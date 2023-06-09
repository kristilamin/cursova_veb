# Generated by Django 4.2 on 2023-05-03 19:01

from django.db import migrations, models
import django.db.models.deletion
import homepage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.TextField(verbose_name="Ім'я замовника")),
                ('phone', models.TextField(verbose_name='Номер телефону')),
                ('email', models.TextField(verbose_name='Електронна пошта')),
                ('password', models.TextField(verbose_name='Пароль')),
                ('city', models.TextField(verbose_name='Місто замовника')),
                ('new_post_number', models.TextField(verbose_name='Номер відділення нової пошти')),
            ],
            options={
                'verbose_name': 'Дані про замовника',
                'verbose_name_plural': 'Дані про замовників',
                'db_table': 'customer',
            },
        ),
        migrations.CreateModel(
            name='Surovuna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surovuna_name', models.TextField(verbose_name='Назва сировини')),
                ('quantity_on_plant', models.IntegerField(verbose_name='Кількість сировини')),
                ('vurobnucha_price_kg', models.IntegerField(verbose_name='Ціна за кілограм сировини')),
                ('vurobnucha_price_general_kg', models.IntegerField(verbose_name='Загальна ціна за сировину')),
                ('delivery_price', models.IntegerField(verbose_name='Ціна доставки')),
                ('delivery_name', models.TextField(verbose_name='Постачальник')),
            ],
            options={
                'verbose_name': 'Дані про сировину',
                'verbose_name_plural': 'Дані про сировину',
                'db_table': 'surovuna',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.TextField(verbose_name='Назва продукту')),
                ('wine_type', models.TextField(verbose_name='Тип')),
                ('quantity_on_plant', models.IntegerField(verbose_name='Кількість на заводі')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата виготовлення')),
                ('price', models.IntegerField(verbose_name='Ціна')),
                ('price_for_all', models.IntegerField(verbose_name='Ціна за всі одиниці продукту')),
                ('surovuna_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='homepage.surovuna', verbose_name='Ідентифікатор сировини')),
            ],
            options={
                'verbose_name': 'Доступний продукт',
                'verbose_name_plural': 'Доступні продукти',
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_of_product', models.IntegerField(verbose_name='Кількість продукту')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата замовлення')),
                ('last_updated_at', models.DateTimeField(blank=True, null=True, verbose_name='Востаннє змінено')),
                ('order_status', models.CharField(max_length=20, verbose_name='Статус замовлення', choices=homepage.models.STATUS_CHOICES, default='open')),
                # ('order_status', models.TextField(validators=[homepage.models.status_validator], verbose_name='Статус замовлення')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='homepage.customer', verbose_name='Замовник')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='homepage.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Замовлення',
                'verbose_name_plural': 'Замовлення',
                'db_table': 'order',
            },
        ),
    ]
