from django.contrib.auth.models import User
from django.db import models

# Create your models here.

CUSTOMER_STATUS = [
    ('CU', 'عميل'),
    ('AD', 'مسؤول'),
    ('DL', 'سائق توصيل'),
    ('SH', 'طباخ'),
]

ORDER_STATUS = [
    ('NO', 'لم يتم ارسالة بعد'),
    ('UR', 'تم استلام طلبك بنجاح'),
    ('BA', 'تم تأكيد طلبك'),
    ('UP', ' طلبك قيد التحضر '),
    ('BS', 'طلبك في الطريق اليك'),
    ('DE', 'تم توصيل طلبك بنجاح'),
    ('FH', 'تم إلغاء طلبك'),
]

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)
    status_customer = models.CharField(max_length=2, choices=CUSTOMER_STATUS, default='CU')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    discount_price = models.FloatField(blank=True, null=True)
    digital = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(null=False, blank=False)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=True)
    transaction_id = models.CharField(max_length=100, null=True)
    status_order = models.CharField(max_length=2, choices=ORDER_STATUS, default='NO')
    booking_driver = models.BooleanField(default=False, null=True, blank=True)
    driver = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def shipping(self):
        shipping = False
        orderitem = self.orderitem_set.all()
        for i in orderitem:
            if i.product.digital == False:
                shipping = True
        return shipping

    @property
    def get_cart_total(self):
        orderitem = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitem])
        return total

    @property
    def get_cart_items(self):
        orderitem = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitem])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.price * self.quantity
        return total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)