from django.forms import ModelForm
from .models import jrny
from django import forms


class AddJourney(ModelForm):
    class Meta:
        model = jrny
        fields = ['start','destination','date','time','number']
