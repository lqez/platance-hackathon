from django.contrib import admin
from models import Rider, Menu, Order, MenuOrder, DeliveryTime


class RiderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'level', ]
    search_fields = ['name', ]
    ordering = ('-id',)
admin.site.register(Rider, RiderAdmin)


class MenuAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', ]
    search_fields = ['name', ]
    ordering = ('-id',)
admin.site.register(Menu, MenuAdmin)


class DeliveryTimeAdmin(admin.ModelAdmin):
    list_display = ['id', 'time', ]
    ordering = ('-id',)
admin.site.register(DeliveryTime, DeliveryTimeAdmin)


class MenuOrderInline(admin.TabularInline):
    model = MenuOrder
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'requestDate', 'requestTime', 'deliveryTime', 'deliveryCompleteTime', ]
    search_fields = ['requestDate', ]
    inlines = (MenuOrderInline, )
    ordering = ('-id',)
admin.site.register(Order, OrderAdmin)
