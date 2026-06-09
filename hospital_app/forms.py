from django import forms
from .models import Booking

class Booking_form(forms.ModelForm):
    class Meta:
        widgets = {
            'booking_date':forms.DateInput(
                attrs={'type':'date'}
            )
        }
        model = Booking
        fields = '__all__'