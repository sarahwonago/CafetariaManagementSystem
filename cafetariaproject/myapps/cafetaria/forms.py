from django import forms

from .models import UserDinningTable

class UserDinningForm(forms.ModelForm):
    class Meta:
        model = UserDinningTable
        fields = ["dinning_table"]