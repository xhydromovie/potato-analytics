from .models import IgritItem
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.core.serializers import serialize
from django.forms.models import model_to_dict

def igrit_chart(request, num=80):
    items = IgritItem.objects.filter(price_bool=True, item_type="Sprzedaż").reverse().values('id', 'price')
    items_list = list(items)
    
    # context = {
    #     "objects_list": items[:num]
    # }
    # return render(request, "index.html", context)
    return JsonResponse(items_list[-50:], safe=False)

def igrit_chart_but(request):
    items_buy = IgritItem.objects.filter(price_bool=True, item_type="Kupno").reverse().values('id', 'price')
    items_buy_list = list(items_buy)
    return JsonResponse(items_buy_list[-50:], safe=False)

def display_chart(request):
    return render(request, 'index.html')