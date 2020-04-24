from django.db import models


class Product(models.Model):
    code = models.CharField(max_length=10,unique=True,primary_key=True)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    inventory = models.IntegerField(default=0)

    def increase_inventory(self, amount):
        self.inventory += amount

    def decrease_inventory(self, amount):
        self.inventory += amount


class Customer(models.Model):
    user = models.OneToOneField('auth_user',on_delete=models.PROTECT)
    phone = models.CharField(max_length=20)
    address = models.TextField
    balance = models.IntegerField(default=20000)

    def deposit(self, amount):
        self.balance += amount

    def spend(self, amount):
        self.balance += amount


class OrderRow(models.Model):
    product = models.ForeignKey('Product',on_delete=models.PROTECT)
    order = models.ForeignKey('Order',on_delete=models.PROTECT)
    amount = models.IntegerField


class Order(models.Model):
    # Status values. DO NOT EDIT
    STATUS_SHOPPING = 1
    STATUS_SUBMITTED = 2
    STATUS_CANCELED = 3
    STATUS_SENT = 4
    status_choices = (
        (STATUS_SHOPPING,'(درحال خرید)'),
        (STATUS_SUBMITTED, '(ثبت شده)'),
        (STATUS_CANCELED, '(لغو شده)'),
        (STATUS_SENT, '(ارسال شده))')
    )
    
    customer = models.ForeignKey('Customer',on_delete=models.PROTECT)
    order_time = models.DateTimeField()
    total_price = models.IntegerField()
    status = models.IntegerField(choices=status_choices)
    rows = models.ForeignKey('OrderRow')
    @staticmethod
    def initiate(customer):
        pass

    def add_product(self, product, amount):
        pass

    def remove_product(self, product, amount=None):
        pass

    def submit(self):
        pass

    def cancel(self):
        pass

    def send(self):
        pass
