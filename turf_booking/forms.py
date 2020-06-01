from django import forms
from .models import Turf, Slot, Bookie

# Form for creation of new Turf:
class NewTurf(forms.ModelForm):
    class Meta:
        model = Turf
        fields = ['name', 'location', 'password', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control col-lg-12'}),
            'location': forms.Textarea(attrs={'class': 'form-control col-lg-12'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control col-lg-12'}),
        }


# Form for create of new slot:
class NewSlot(forms.ModelForm):
    class Meta:
        model = Slot
        fields = ['timing', 'date']
        widgets = {
            'date': forms.DateTimeInput(attrs={'class': 'datetime-input'})
        }


# Form for creation of new User:
class NewUser(forms.ModelForm):
    class Meta:
        model = Bookie
        fields = ['name', 'phone_number', 'password']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control col-lg-12'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control col-lg-12'}),
        }


class LogUser(forms.ModelForm):
    class Meta:
        model = Bookie
        fields = ['name', 'password']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control col-lg-12'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control col-lg-12'}),
        }


class LogTurf(forms.ModelForm):
    class Meta:
        model = Turf
        fields = ['name', 'password']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control col-lg-12'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control col-lg-12'}),
        }
