from django import forms
from .models import Masuk
from datetime import datetime

class MasukForms(forms.ModelForm):
    class Meta:
        model = Masuk
        fields = ["id"]