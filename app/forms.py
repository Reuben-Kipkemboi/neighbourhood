from django import forms
from . models import *

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']