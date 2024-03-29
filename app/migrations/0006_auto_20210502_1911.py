# Generated by Django 3.2 on 2021-05-02 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_customer_status_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='status_customer',
            field=models.CharField(choices=[('CU', 'عميل'), ('AD', 'مسؤول'), ('DL', 'سائق توصيل'), ('SH', 'طباخ')], default='NO', max_length=2),
        ),
        migrations.AlterField(
            model_name='order',
            name='status_order',
            field=models.CharField(choices=[('NO', 'لم يم ارسالة بعد'), ('UR', 'قيد المراجعة'), ('BA', 'تمت الموافة'), ('UP', 'قيد التحضر'), ('BS', 'تم الارسال'), ('DE', 'تم التوصيل')], default='UR', max_length=2),
        ),
    ]
