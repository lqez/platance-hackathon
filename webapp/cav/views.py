from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from models import DeliveryTime, Order


def index(request):
    return render(request, 'index.html', {
        "deliveryTimes": DeliveryTime.objects.all(),
    })


def fetch(request):
    date = request.GET.get('date')
    time = request.GET.get('time')

    deliveryTime = date + ' ' + time
    orders = []

    for order in Order.objects.filter(deliveryTime=deliveryTime):
        orders.append({
            'latitude': order.latitude,
            'longitude': order.longitude,
            'count': len(order.menuorder_set.all()),
        })

    return JsonResponse({
        'orders': orders,
    })
