from django import forms
from django.contrib.auth.models import User
from .models import Profile
######################################################

class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email']

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phoneNumber','address1','address2','image']

class CreateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password']