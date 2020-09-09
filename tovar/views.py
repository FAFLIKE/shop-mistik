from django.shortcuts import render
from .models import modelGoods

def mainPage(request):
    a = modelGoods.objects.all()
    context = {'products': a,}
    return render(request, 'tovar/goods/listGoods.html', context)

def infoAllGoods(request):
    a = modelGoods.objects.all()
    context = {'products': a,}
    return render(request, 'tovar/goods/listGoods.html', context)

def infoGoods(request, numberGoods):
    a = modelGoods.objects.all()
    context = {'products': a[numberGoods], 'numberGoods': numberGoods,}
    return render(request, 'tovar/goods/vievGoods.html', context)
    