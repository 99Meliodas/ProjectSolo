from django import forms
from .models import feedback

class FeedbackForm(forms.ModelForm):

    class Meta:
        model = feedback
        fields = ('name', 'email', 'phone_number', 'message')
        widgets = {
            'name' : forms.TextInput(attrs={'placeholder' : 'Name'}),
            'email' : forms.EmailInput(attrs={'placeholder' : 'Email'}),
            'phone number' : forms.Select(attrs={'placeholder' : 'phone number'}),
            'message' : forms.TextInput(attrs={'placeholder' : 'Message'}),
        }
        labels = {
           'name' : '',
           'email' : '',
           'phone number' : '',
           'message' : '',
        }