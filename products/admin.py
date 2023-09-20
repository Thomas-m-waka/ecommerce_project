from django.contrib import admin

# Register your models here.


from .models import Flower, Order, OrderItem, Payment, Review
admin.site.register(Flower)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Payment)
admin.site.register(Review)
