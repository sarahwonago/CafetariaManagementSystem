from django import forms
from myapps.cafetaria.models import Category


class CategoryForm(forms.ModelForm):

    """
    CategoryForm for adding new categories.
    """
    class Meta:
        model = Category
        fields = '__all__'