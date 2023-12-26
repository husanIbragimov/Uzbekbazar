from django import forms
from .models import OrderOneClick


class OrderOneClickForm(forms.ModelForm):
    class Meta:
        model = OrderOneClick
        fields = ('first_name', 'last_name', 'phone_number')