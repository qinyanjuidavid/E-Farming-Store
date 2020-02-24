from django.contrib import admin
from business.models import Item,OrderItem,Order,BillingAddress

class ProductAdmin(admin.ModelAdmin):
    search_fields=['item_name']
    list_display=('item_name','price','discount_price')
    list_filter=('category')
admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(BillingAddress)
