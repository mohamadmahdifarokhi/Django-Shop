from django.contrib import admin
from .models import Order, OrderItem, Coupon


# bara inke item va order zer ham bashan
# TabularInline   jadvali
# StackedInline   khati
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'paid', 'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    # zer order ino neshon bede
    inlines = [OrderItemInline]


admin.site.register(Coupon)
