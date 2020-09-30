from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from tovar.models import modelGoods
from cart.cart import Cart
from django.conf import settings

def mainPage(request):
    goods = modelGoods.objects.all()
    cart = Cart(request).cart
    context = {'products': goods, 'cart': cart}
    if request.method == "POST":
        request.session[settings.CART_SESSION_ID] = {}
    return render(request, 'shop_mistik/mainPage.html', context)
