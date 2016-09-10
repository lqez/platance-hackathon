from django.http import JsonResponse
from django.shortcuts import render
from models import DeliveryTime, Order
from random import randint


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


def simulate(request):
    date = request.GET.get('date')
    time = request.GET.get('time')
    algorithm = request.GET.get('algorithm')
    riders = int(request.GET.get('riders', 1))

    deliveryTime = date + ' ' + time
    result = []

    orders = Order.objects.filter(deliveryTime=deliveryTime)

    for order in orders:
        result.append({
            'latitude': order.latitude,
            'longitude': order.longitude,
            'count': len(order.menuorder_set.all()),
            'color': randint(1, riders),
        })

    return JsonResponse({
        'result': result,
    })
