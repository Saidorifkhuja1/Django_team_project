# Generated by Django 4.2 on 2023-08-01 03:14

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_catalog', '0001_initial'),
        ('app_discounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255, verbose_name='Фамилия Имя Отчество')),
                ('phone_number', models.CharField(blank=True, help_text='Contact phone number', max_length=20, verbose_name='Телефон')),
                ('email', models.EmailField(max_length=50, verbose_name='E-mail')),
                ('city', models.CharField(blank=True, max_length=100, null=True, verbose_name='Город')),
                ('address', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Адрес доставки')),
                ('delivery', models.CharField(choices=[('Обычная доставка', 'Обычная доставка'), ('Экспресс доставка', 'Экспресс доставка')], default='Обычная доставка', max_length=100, verbose_name='Способ доставки')),
                ('delivery_cost', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Стоимость доставки')),
                ('payment', models.CharField(choices=[('Онлайн картой', 'Онлайн картой'), ('Онлайн со случайного чужого счета', 'Онлайн со случайного чужого счета')], default='Онлайн картой', max_length=100, verbose_name='Способ Оплаты')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий к заказу')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Дата создания заказа')),
                ('status', models.CharField(choices=[('Не оплачен', 'Не оплачен'), ('Оплачен', 'Оплачен')], default='Не оплачен', max_length=25, verbose_name='Статус заказа')),
                ('discount', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('coupon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='app_discounts.coupon')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Количество товара')),
                ('price', models.DecimalField(decimal_places=2, default=1, max_digits=10, verbose_name='Цена товара')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='app_orders.order', verbose_name='Заказ')),
                ('product_in_shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='app_catalog.productinshop', verbose_name='Товар')),
            ],
        ),
    ]
