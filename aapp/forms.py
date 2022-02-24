from django import forms
from django.forms import ModelForm
from .models import Serial

#Create Forms
class SerialForm(ModelForm):
    class Meta:
        model = Serial
        #fields = "__all__"
        fields = ('name', 'address', 'zip_code', 'phone', 'web', 'email_address')       
        