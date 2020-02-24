from django.urls import path
from business import views
app_name="business"

urlpatterns=[
path('',views.Home,name='home'),
path('products/',views.Products,name="product"),
path('product/details/<id>/',views.ProductDetailsView,name="details"),
path('item/<id>/',views.AddToCart,name='add_to_cart'),
path('delete/item/<id>/',views.RemoveFromCart,name="remove"),
path('cart/',views.OrderSummary,name='cart'),
path('remove/<id>/',views.RemoveSingleItem,name="remove_single"),
path('checkout/',views.CheckOutView,name="checkout")
]
