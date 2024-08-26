from django import forms
from myapps.cafetaria.models import Category, FoodItem, DiningTable, Order


class CategoryForm(forms.ModelForm):

    """
    CategoryForm for adding new categories.
    """
    class Meta:
        model = Category
        fields = '__all__'



class FoodItemForm(forms.ModelForm):

    """
    FoodItemForm for adding new fooditem.
    """
    class Meta:
        model = FoodItem
        fields = [
            "name",
            "description",
            "price",
            "image",
            "is_available",
        ]
    

class DinningTableForm(forms.ModelForm):

    """
    DinningTableForm for adding new dinningtables.
    """
    class Meta:
        model = DiningTable
        fields = [
            "table_number",
        ]

class UpdateOrderForm(forms.ModelForm):
    """
    OrderForm for updating an order.
    """

    class Meta:
        model = Order
        fields = [
            "estimated_time",
            "status",
        ]