from django.forms import ModelForm,widgets
from .models import Customer

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['datetime','no_of_diners','name','email','phone_no']
        widgets = {
            'datetime': widgets.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'no_of_diners': widgets.NumberInput(attrs={'class': 'form-control'}),
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'email': widgets.EmailInput(attrs={'class': 'form-control'}),
            'phone_no': widgets.NumberInput(attrs={'class': 'form-control'}),
            'special_request': widgets.Textarea(attrs={'class': 'form-control'}),
        }
