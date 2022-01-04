from django.shortcuts import redirect, render
from accounts.models import AddProducts, Customer, User
from .models import Order
# Create your views here.
def store(request):
    products=AddProducts.objects.all()
    return render(request, 'store/store.html', {'products':products})

def storeproduct(request):
    if not request.user.is_authenticated:
        return render(request,'mainbase.html')
    else:
        count_products=AddProducts.objects.all().count()
    return render(request, 'mainbase.html', {'count_products':count_products})

def cart(request):
    if request.user.is_authenticated:
        print(User.objects.all())
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,completed=False)
        items = order.orderitem_set.all()
    else:
        items=[]
        order={'get_cart_total':0,"get_cart_items":0}
    return render(request, 'store/cart.html', {'items':items,"order":order})
