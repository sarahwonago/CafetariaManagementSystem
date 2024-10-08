

from django.urls import path

from .views import (home_view, handle_unauthorized_access, addtocart_view, cart_view, 
                    food_items_view,checkout_view, order_complete_view, increase_orderitem_view,
                    decrease_orderitem_view, remove_item_view, order_history_view, order_receipt_view,
                    review_dish_view, food_detail_view, customer_points_view, customer_notifications_view,
                    marknotification_read_view)

app_name="cafetaria"

urlpatterns=[
    path("", home_view, name="home"),
    path("notifications/", customer_notifications_view, name="notifications"),
    path("mark-as-read/<int:notification_id>/", marknotification_read_view, name="mark-read"),
    path("points/", customer_points_view, name="points"),
    path("addtocart/<int:food_id>/", addtocart_view, name="addtocart"),
    path("food/", food_items_view, name="food"),
    path("food-detail/<int:food_id>/", food_detail_view, name="food-detail"),
    path("cart/", cart_view, name="cart"),
    path("order-history/", order_history_view, name="order-history"),
    path("order-review/<int:order_id>/", review_dish_view, name="review-order"),
    path("order-receipt/<int:order_id>/", order_receipt_view, name="order-reciept"),
    path("increase-order/<int:item_id>/", increase_orderitem_view, name="increase-quantity"),
    path("decrease-order/<int:item_id>/", decrease_orderitem_view, name="decrease-quantity"),
    path("remove-item/<int:item_id>/", remove_item_view, name="remove-item"),
    path("checkout/", checkout_view, name="checkout"),
    path("order-complete/<int:order_id>/", order_complete_view, name="order-complete"),
    path("unauthorized/", handle_unauthorized_access, name="handle_unauthorized_access"),
]