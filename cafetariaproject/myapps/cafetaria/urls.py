

from django.urls import path

from .views import home_view, handle_unauthorized_access, addtocart_view, order_summary_view, customer_view

app_name="cafetaria"

urlpatterns=[
    path("", home_view, name="home"),
    path("addtocart/<int:food_id>/", addtocart_view, name="addtocart"),
    path("food/", customer_view, name="food"),
    path("ordersummary/", order_summary_view, name="order-summary"),
    path("unauthorized/", handle_unauthorized_access, name="handle_unauthorized_access"),
]