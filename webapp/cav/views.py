from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from models import DeliveryTime, Order
from random import shuffle
import os
import subprocess


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
    orders = list(Order.objects.filter(deliveryTime=deliveryTime))

    # Oh shit my hard-coded switch cases...
    result = []
    if algorithm == 'random':
        def chunkIt(seq, num):
            avg = len(seq) / float(num)
            out = []
            last = 0.0

            while last < len(seq):
                out.append(seq[int(last):int(last + avg)])
                last += avg

            return out

        shuffle(orders)
        result = chunkIt(orders, riders)
    elif algorithm == 'kmean':
        py = os.path.dirname(settings.BASE_DIR) + '/engine/kmean/clustering.py'
        text = "{}\n{}\n".format(riders, len(orders))
        for order in orders:
            text += "{} {}\n".format(order.latitude, order.longitude)
        proc = subprocess.Popen(['python', py], stdout=subprocess.PIPE, stdin=subprocess.PIPE)
        proc.stdin.write(text)
        proc.stdin.close()

        outputs = proc.stdout.read()
        for line in outputs.strip().split("\n"):
            order_list = []
            for idx in line.strip().split(" "):
                order = orders[int(idx)]
                order_list.append(order)
            result.append(order_list)
        proc.wait()
    elif algorithm == '13k':
        pass

    # Finalize
    final = []
    for path in result:
        arr = []
        for obj in path:
            arr.append({
                'latitude': obj.latitude,
                'longitude': obj.longitude,
            })
        final.append(arr)

    return JsonResponse({
        'result': final,
    })
