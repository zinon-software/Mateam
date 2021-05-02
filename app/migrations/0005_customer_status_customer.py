# Generated by Django 3.2 on 2021-05-02 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_order_status_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='status_customer',
            field=models.CharField(choices=[('CU', 'عميل'), ('AD', 'مسؤول'), ('DL', 'سائق توصيل'), ('SH', 'طباخ')], default='CU', max_length=2),
        ),
    ]
