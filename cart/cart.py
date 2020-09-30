from django.shortcuts import get_object_or_404
from decimal import Decimal
from django.conf import settings
from tovar.models import modelGoods

class Cart(object):

    def __init__(self, request):
        cart = request.session.get(settings.CART_SESSION_ID)
        if not cart:
            request.session[settings.CART_SESSION_ID] = {}
            cart = request.session.get(settings.CART_SESSION_ID)
        self.cart = cart

    def add(self, request, numberGoods, count):
        cart = self.cart
        cart[numberGoods] = count
        request.session[settings.CART_SESSION_ID] = cart

    def refresh(self, request):
        cart = self.cart
        goods = modelGoods.objects.all()
        goods_exists=[]
        goods_in_cart=list(cart.keys())
        for key in goods:
            goods_id = key.id
            goods_exists.append(str(goods_id))
        for key in goods_in_cart:
            if not key in goods_exists:
                cart.pop(key, 'none')
        request.session[settings.CART_SESSION_ID] = cart

    def get(self, request):
        cart = self.cart
        products = {}
        for key in cart:
            products[key] = modelGoods.objects.filter(id=key).first()
        return products