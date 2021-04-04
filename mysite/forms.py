from .models import Announcement
from django import forms
from django.forms.widgets import ChoiceWidget, HiddenInput, TextInput, Textarea, NumberInput


class UpdateAddForm(forms.ModelForm):
    
    class Meta:
        model = Announcement
        fields = ['title','region','district','location','Beds','Bathroom','Property_type','status','Agents','modum','image','Price','phone','Garage']
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control h6'}),
            'region':forms.Select(attrs={'class':'form-control'}),
            'district':forms.Select(attrs={'class':'form-control'}),
            'Property_type':forms.Select(attrs={'class':'form-control'}),
            'status':forms.Select(attrs={'class':'form-control'}),          
            'image':forms.FileInput(attrs={'class':'form-control'}),
            'location':forms.TextInput(attrs={'class':'form-control'}),
            'Agents':forms.TextInput(attrs={'class':'form-control'}),
            'Beds':forms.NumberInput(attrs={'class':'form-control'}),
            'Bathroom':forms.NumberInput(attrs={'class':'form-control'}),
            'Phone':forms.NumberInput(attrs={'class':'form-control'}),
            'Garage':forms.NumberInput(attrs={'class':'form-control'}),
            'modum':forms.Textarea(attrs={'class':'form-control'}),
            'Price':forms.NumberInput(attrs={'class':'form-control'}),
        }
        
# class ActorSearchForm(forms.Form):
#     search_text =  forms.CharField(
#                     required = False,
#                     widget=forms.TextInput(attrs={
#                         'placeholder': 'City/Locality Name',
#                         'class':'form-control',
#                         'name':'keyvalue'
#                     })
#                 )
class ActorSearchForm(forms.Form):
    search_text =  forms.CharField(
                    required = False,
                    label='location',
                    widget=forms.TextInput(attrs={'placeholder': 'City/LocatilyName here!','class':'form-control'})
                  )

    # search_age_exact = forms.IntegerField(
    #                 required = False,
    #                 label='min price (exact match)!'
    #               )

    # search_age_min = forms.IntegerField(
    #                 required = False,
    #                 label='Min price'
    #               )


    # search_age_max = forms.IntegerField(
    #                 required = False,
    #                 label='Max price'
    #               )
