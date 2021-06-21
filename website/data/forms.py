from django import forms
from django.forms import ModelForm
from .models import Order, Custemer
from django.utils.translation import gettext_lazy as _ 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

        widgets = {
            'custemer_id':forms.Select(attrs={'class':'form-control'}),
            'product_id':forms.Select(attrs={'class':'form-control'}),
            'status':forms.Select(attrs={'class':'form-control'}),
        }

        labels = {
            'custemer_id':'Konsumen',
            'product_id':'Produk',
            'status':'Status',
        }

class CustemerForm(ModelForm):
    class Meta:
        model = Custemer
        fields = '__all__'

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'phone':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }

        
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2',)

        labels = {
            'username': _('Username'),
            'first_name': _('Nama Depan'),
            'last_name': _('Nama Belakang'),
            'email': _('Email'),
        }

    
    