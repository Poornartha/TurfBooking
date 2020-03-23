from django import forms
from .models import Turf, Slot, Bookie


# Form for creation of new Turf:
class NewTurf(forms.ModelForm):
    class Meta:
        model = Turf
        fields = "__all__"


# Form for create of new slot:
class NewSlot(forms.ModelForm):
    class Meta:
        model = Slot
        fields = ['timing']


# Form for creation of new User:
class NewUser(forms.ModelForm):
    class Meta:
        model = Bookie
        fields = ['name', 'phone_number', 'password']


class LogUser(forms.ModelForm):
    class Meta:
        model = Bookie
        fields = ['name', 'password']
