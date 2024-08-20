from django.urls import path

from .views import (home_view, categories_view, add_category_view, delete_category_view,
                    update_category_view)

app_name = 'cafeadmin'

urlpatterns = [
    path("", home_view, name="home"),
    path("categories/", categories_view, name="categories"),
    path("add_category/", add_category_view, name="add-category"),
    path("delete_category/<int:category_id>/", delete_category_view, name="delete-category"),
    path("update_category/<int:category_id>/", update_category_view, name="update-category"),
]   