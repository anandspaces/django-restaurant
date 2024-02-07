# new
from django.forms import ModelForm,widgets
from .models import Customer

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        widgets = {
            'datetime': widgets.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'no_of_diners': widgets.NumberInput(attrs={'class': 'form-control'}),
            'first_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'last_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'email': widgets.EmailInput(attrs={'class': 'form-control'}),
            'phone_no': widgets.NumberInput(attrs={'class': 'form-control'}),
        }
