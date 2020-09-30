from django import template
from tovar.models import modelGoods
register = template.Library()

@register.filter
def takeByKeyStr(dicti, key):
    dict_value = dicti[str(key)]  
    return dict_value

@register.filter
def takeByKey(dicti, key):
    dict_value = dicti[key]
    return dict_value


@register.filter
def multiply(a, b):
    try:
        c = float(a)*float(b)
    except:
        c = "Can't convert to float()"
    return c