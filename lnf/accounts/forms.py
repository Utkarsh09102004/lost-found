from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import Item


class SignUpForm(UserCreationForm):
    password2= forms.CharField(label='Confirm Password (again)',widget=forms.PasswordInput)
    class Meta:
        model = User
        fields =['username', 'first_name','last_name','email']
        labels= {'email':'Email'}


class EditUserProfileForm(UserChangeForm):
    password= None
    class  Meta:
        model= User
        fields =['username','first_name','last_name','email','date_joined','last_login']
        labels= {'email':'Email'}


class LostItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('title', 'description', 'image', 'location', 'date_lost_or_found', 'contact_email')
        # You can customize the form fields' labels, widgets, and additional validation if needed

class FoundItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('title', 'description', 'image', 'location', 'date_lost_or_found', 'contact_email')
        # You can customize the form fields' labels, widgets, and additional validation if needed
