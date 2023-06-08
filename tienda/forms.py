from django import forms
from .models import Product

class FormularioPost(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name' , 'slug' , 'category','image' , 'excerpt' , 'detail' , 'price' , 'availalble' )
