from django.urls import path

from .views import (home_view, categories_view, add_category_view, delete_category_view,
                    update_category_view, category_fooditem_view, add_fooditem_view,
                    delete_fooditem_view, update_fooditem_view, dinning_table_view,
                    add_dinningtable_view, update_dinningtable_view, delete_dinningtable_view,
                    orders_view, confirm_orders_view, reviews_view)

app_name = 'cafeadmin'

urlpatterns = [
    path("", home_view, name="home"),
    path("reviews/", reviews_view, name="reviews"),
    path("orders/", orders_view, name="customer-orders"),
    path("confirm-order/<int:order_id>/", confirm_orders_view, name="confirm-order"),
    path("categories/", categories_view, name="categories"),
    path("add_category/", add_category_view, name="add-category"),
    path("delete_category/<int:category_id>/", delete_category_view, name="delete-category"),
    path("update_category/<int:category_id>/", update_category_view, name="update-category"),
    path("category/<int:category_id>/fooditems/", category_fooditem_view, name="category-items"),
    path("add_fooditem/<int:category_id>/", add_fooditem_view, name="add-fooditem"),
    path("delete_fooditem/<int:fooditem_id>/<int:category_id>/", delete_fooditem_view, name="delete-fooditem"),
    path("update_fooditem/<int:fooditem_id>/<int:category_id>/", update_fooditem_view, name="update-fooditem"),
    path("dinningtables/", dinning_table_view, name="dinningtables"),
    path("add_dinningtable/", add_dinningtable_view, name="add-dinning-table"),
    path("delete_dinningtable/<int:table_id>/", delete_dinningtable_view, name="delete-dinning-table"),
    path("update_dinningtable/<int:table_id>/", update_dinningtable_view, name="update-dinning-table"),
]   