from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from business.models import Item,OrderItem,Order,BillingAddress
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from business.forms import CheckOutForm
from django.contrib import messages


def Home(request):
    item=Item.objects.filter(offer=True)
    context={
    "item":item
    }
    return render(request,'business/home.html',context)
@login_required
def CheckOutView(request):
    form=CheckOutForm()
    if Order.objects.get(user=request.user,ordered=False):
        if request.method=="POST":
            form=CheckOutForm(request.POST or None)
            if form.is_valid():
                street_address=form.cleaned_data.get('street_address')
                apartment_address=form.cleaned_data.get('apartment_address')
                country=form.cleaned_data.get("country")
                zip=form.cleaned_data.get('zip')
                payment_option=form.cleaned_data.get('payment_option')
                billing_address=BillingAddress(
                user=request.user,
                street_address=street_address,
                apartment_address=apartment_address,
                country=country,
                zip=zip
                )
                billing_address.save()
                messages.success(request,'Your information was successfully submitted.')

    context={
    'form':form
    }
    return render(request,'business/checkout.html',context)


def Products(request):
    item_obj=Item.objects.all()
    context={
    'item_obj':item_obj
    }
    return render(request,'business/products.html',context)
@login_required
def ProductDetailsView(request,id):
    item_details=Item.objects.get(id=id)
    context={
    'item':item_details
    }
    return render(request,'business/product_details.html',context)
@login_required
def AddToCart(request,id):
    item=Item.objects.get(id=id)
    order_item,created=OrderItem.objects.get_or_create(item=item,user=request.user,ordered=False)
    order=Order.objects.filter(user=request.user,ordered=False)
    if order.exists():
        order=order[0]
        if order.items.filter(item__id=item.id).exists():
            order_item.quantity+=1
            order_item.save()
            #messages.info(request,'The item was successfully added to your cart.')
        else:
            order.items.add(order_item)
    else:
        date_ordered=timezone.now()
        order=Order.objects.create(user=request.user,date_ordered=date_ordered)
        order.items.add(order_item)
        return HttpResponseRedirect(f'/cart/')

    context={
    'item':item
    }
    messages.success(request,'The item was successfully added to your cart.')
    return HttpResponseRedirect(f'/cart/')
@login_required
def RemoveFromCart(request,id):
    item=Item.objects.get(id=id)
    order_item=OrderItem.objects.get_or_create(item=item,user=request.user,ordered=False)
    order=Order.objects.filter(user=request.user,ordered=False)
    if order.exists():
        order=order[0]
        if order.items.filter(item__id=item.id).exists():
            order_item=OrderItem.objects.filter(user=request.user,ordered=False)[0]
            order.items.remove(order_item)
        else:
            print('Successfully  deleted')
    else:
        print("successfully deleted")
    messages.warning(request,'Your order item was successfully removed from the cart.')
    return HttpResponseRedirect(f'/product/details/{id}/')
@login_required
def RemoveSingleItem(request,id):
    item=Item.objects.get(id=id)
    order_item=OrderItem.objects.get_or_create(item=item,user=request.user,ordered=False)
    order=Order.objects.filter(user=request.user,ordered=False)
    if order.exists():
        order=order[0]
        if order.items.filter(item__id=item.id).exists():
            order_item=OrderItem.objects.filter(user=request.user,ordered=False)[0]
            if order_item.quantity>1:
                order_item.quantity -= 1
                order_item.save()
                messages.info(request,'The item quantity was successfully update.')
            else:
                order.items.remove(order_item)
                messages.warning(request,'The item was removed from your cart.')
        else:
            print("success")
    else:
        print('Success')
    return HttpResponseRedirect('/cart/')
@login_required
def OrderSummary(request):
    sum=Order.objects.filter(user=request.user,ordered=False)
    context={
    'sum':sum
    }
    return render(request,'business/summary.html',context)
