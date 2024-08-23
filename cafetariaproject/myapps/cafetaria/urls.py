

from django.urls import path

from .views import (home_view, handle_unauthorized_access, addtocart_view, order_summary_view, 
                    customer_view,checkout_view, order_complete_view)

app_name="cafetaria"

urlpatterns=[
    path("", home_view, name="home"),
    path("addtocart/<int:food_id>/", addtocart_view, name="addtocart"),
    path("food/", customer_view, name="food"),
    path("customerorders/", order_summary_view, name="order-summary"),
    path("checkout/", checkout_view, name="checkout"),
    path("order-complete/<int:order_id>/", order_complete_view, name="order-complete"),
    path("unauthorized/", handle_unauthorized_access, name="handle_unauthorized_access"),
]