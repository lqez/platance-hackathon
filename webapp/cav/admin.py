from django.contrib import admin
from models import Rider, Menu, Order


class RiderAdmin(admin.ModelAdmin):
    list_display = ['name', 'level', ]
    search_fields = ['name', ]
    ordering = ('-id',)
admin.site.register(Rider, RiderAdmin)


class MenuAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', ]
    search_fields = ['name', ]
    ordering = ('-id',)
admin.site.register(Menu, MenuAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ['requestDate', 'requestTime', 'deliveryTime', 'deliveryCompleteTime', ]
    search_fields = ['requestDate', ]
    ordering = ('-id',)
admin.site.register(Order, OrderAdmin)
