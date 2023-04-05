from django import forms

from utilities.forms import BootstrapMixin


class CreateUserForm(forms.Form):
    username = forms.CharField(
        max_length=50,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        })
    )
    password = forms.CharField(
        max_length=50,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        })
    )
