from django import forms

from .models import UserDinningTable, Review

class UserDinningForm(forms.ModelForm):
    class Meta:
        model = UserDinningTable
        fields = ["dinning_table"]


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["rating", "comment"]
        widgets = {
            'rating': forms.RadioSelect(choices=[(i, str(i)) for i in range(1, 6)]),
            'comment': forms.Textarea(attrs={'rows': 3}),
        }