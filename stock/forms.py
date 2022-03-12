from django import forms
  
# import GeeksModel from models.py
from .models import RegistrationFormDemant
  
# create a ModelForm
class RegistrationFormDemantForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = RegistrationFormDemant
        fields = "__all__"