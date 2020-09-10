from django.shortcuts import render, get_object_or_404
from .models import modelGoods

def mainPage(request):
    goods = modelGoods.objects.all()
    session = request.session.get('1')
    if session == None:
        request.session['1'] = 0
        session = request.session.get('1')

    session = request.session.get('1')
    request.session['1'] = session+1
    context = {'products': goods, 'session': session,}
    return render(request, 'tovar/mainPage.html', context)

def infoAllGoods(request):
    goods = modelGoods.objects.all()
    context = {'products': goods,}
    return render(request, 'tovar/goods/listGoods.html', context)

def infoGoods(request, numberGoods):
    goods = get_object_or_404(modelGoods, id=numberGoods)
    context = {'products': goods, 'numberGoods': numberGoods,}
    return render(request, 'tovar/goods/vievGoods.html', context)
    