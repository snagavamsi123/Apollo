from django import forms
from django.db.models import fields
from django.forms import ModelForm, widgets
from .models import signup,tickets

class signupform(ModelForm):
    class Meta:
        model = signup
        fields = '__all__'
        widgets={
            'Password':forms.PasswordInput(render_value=True),
        }


class loginform(ModelForm):
    class Meta:
        model = signup
        fields = ('Email','Password')
        widgets={
            'Password':forms.PasswordInput(render_value=True),
        }

class ticketsform(ModelForm):
    class Meta:
        model=tickets
        fields = ('Type','Floor','Desk_No','Description')
        


