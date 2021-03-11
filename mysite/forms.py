from .models import Announcement
from django import forms
from django.forms.widgets import ChoiceWidget, HiddenInput, TextInput, Textarea, NumberInput
class ActorSearchForm(forms.Form):
    search_text =  forms.CharField(
                    required = False,
                    widget=forms.TextInput(attrs={
                        'placeholder': 'City/Locality Name',
                        'class':'form-control',
                        'name':'keyvalue'
                    })
                )

    # search_age_exact = forms.IntegerField(
    #                 required = False,
    #                 label='Search age (exact match)!'
    #               )

    # search_age_min = forms.IntegerField(
    #                 required = False,
    #                 label='Min age'
    #               )


    # search_age_max = forms.IntegerField(
    #                 required = False,
    #                 label='Max age'
    #               )