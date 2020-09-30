from django.urls import path
from . import views

urlpatterns = [
    path('', views.cartViev, name='cartViev'),
 ]