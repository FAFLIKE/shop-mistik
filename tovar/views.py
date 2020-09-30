from django.shortcuts import render, get_object_or_404
from django.conf import settings
from .models import modelGoods
from cart.forms import AddCartF
from cart.cart import Cart

def mainPage(request):
    goods = modelGoods.objects.all()
    context = {'products': goods,}
    return render(request, 'tovar/mainPage.html', context)

def infoAllGoods(request):
    goods = modelGoods.objects.all()
    context = {'products': goods,}
    return render(request, 'tovar/goods/listGoods.html', context)

def infoGoods(request, numberGoods):
    cart_product_form = AddCartF()
    goods = get_object_or_404(modelGoods, id=numberGoods)
    cart = Cart(request).cart
    if request.method == "POST":
        count = int(request.POST.get("count"))
        Cart(request).add(request, numberGoods, count)
    else:
        try:
            count = cart[str(numberGoods)]
        except:
            count = 0
    context = {'products': goods, 'numberGoods': numberGoods, 'cart_product_form': cart_product_form, 'count': count}
    return render(request, 'tovar/goods/vievGoods.html', context)
    