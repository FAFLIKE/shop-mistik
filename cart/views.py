from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from tovar.models import modelGoods
from .cart import Cart
from django.conf import settings

def cartViev(request):
    Cart(request).refresh(request)
    cart = Cart(request).cart
    products = Cart(request).get(request)
    context = {'products': products, 'cart': cart}
    return render(request, 'cart/cart_viev.html', context)