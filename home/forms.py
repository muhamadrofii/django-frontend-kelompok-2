from django import forms
from .models import ContactUs

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control text-white bg-dark border-light placeholder-white', 'placeholder': 'Nama'}),
            'email': forms.EmailInput(attrs={'class': 'form-control text-white bg-dark border-light placeholder-white', 'placeholder': 'Email'}),
            'message': forms.Textarea(attrs={'class': 'form-control text-white bg-dark border-light placeholder-white', 'placeholder': 'Feedback'})
        }
