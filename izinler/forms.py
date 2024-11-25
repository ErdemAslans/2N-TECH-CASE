from django import forms
from izinler.models import Izin

class IzinForm(forms.ModelForm):
    class Meta:
        model = Izin
        fields = ['start_date', 'end_date']
