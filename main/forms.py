from django.forms import ModelForm
from .models import LostItem, FoundItem, CustomUser

class LostForm(ModelForm):
    class Meta:
        model = LostItem
        exclude = ['loser']

    # Add this method to ensure the form is submitted as multipart/form-data
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].widget.attrs.update({'enctype': 'multipart/form-data'})

class FoundForm(ModelForm):
    class Meta:
        model = FoundItem
        exclude = ['founder']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].widget.attrs.update({'enctype': 'multipart/form-data'})


class userRegistration(ModelForm):
    class Meta:
        model= CustomUser
        fields =['username','password','phone_number']