from django import forms
from myapps.cafetaria.models import Category, FoodItem


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