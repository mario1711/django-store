from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Review

class FormularioRegistro(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email' , )


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['contenido']
