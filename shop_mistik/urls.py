from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.mainPage, name='mainPage'),
    path('tovar/', include('tovar.urls'), name='tovar'),
    path('cart/', include('cart.urls'), name='cart'),
    path('admin/', admin.site.urls),
]