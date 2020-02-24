from django.db import models
from accounts.models import User
from django_countries.fields import CountryField


class Item(models.Model):
    item_name=models.CharField(max_length=50,verbose_name="Item")
    description=models.TextField(blank=True,null=True)
    price=models.FloatField(default=0.00)
    discount_price=models.FloatField(default=0.00,blank=True,null=True)
    offer=models.BooleanField(default=False)
    category_choices=(
    ('idk','idk'),
    )
    category=models.CharField(max_length=50,choices=category_choices)
    image=models.ImageField(upload_to='E-farm')

    def __str__(self):
        return self.item_name
class OrderItem(models.Model):
    item=models.ForeignKey(Item,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    ordered=models.BooleanField(default=False)

    def __str__(self):
        return self.item.item_name
    def Total_price(self):
        return self.quantity * self.item.price
    def Total_discount_price(self):
        return self.quantity * self.item.discount_price
    def Amount_saved(self):
        return self.Total_price() - self.Total_discount_price()
    def get_Final_price(self):
        if self.item.discount_price:
            return self.Total_discount_price
        return self.Total_price

class Order(models.Model):
    items=models.ManyToManyField(OrderItem)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    start_date=models.DateTimeField(auto_now_add=True)
    date_ordered=models.DateTimeField()
    ordered=models.BooleanField(default=False)
    billing_address=models.ForeignKey('BillingAddress',on_delete=models.SET_NULL,blank=True,null=True)

    def __str__(self):
        return self.user.username

    '''def Total_Final_price(self):
        total=0
        for order_item in self.items.all():
            if self.order_item.item.discount_price:
                total+=order_item.Total_discount_price
            total+=order_item.Total_price
        return total'''


class BillingAddress(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    street_address=models.CharField(max_length=100)
    apartment_address=models.CharField(max_length=100)
    country=CountryField(multiple=False)
    zip=models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
