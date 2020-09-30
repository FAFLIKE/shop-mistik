from django.urls import path
from . import views

urlpatterns = [
    path('goods/<int:numberGoods>', views.infoGoods, name='vievGoods'),
    path('goods/', views.infoAllGoods, name='listGoods'),
 ]