

from django.contrib import admin
from .models import Category, FoodItem, DiningTable, Order, OrderItem, Review,UserDinningTable

admin.site.register(Category)
admin.site.register(FoodItem)
admin.site.register(DiningTable)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Review)
admin.site.register(UserDinningTable)
