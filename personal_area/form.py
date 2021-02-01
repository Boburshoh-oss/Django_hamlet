from django import forms 
from django.forms.widgets import ChoiceWidget, HiddenInput, TextInput, Textarea
from mysite.models import Region, District, Status, Type 

class AddForm(forms.Form):
    title=forms.CharField(
        max_length=50,
        widget=TextInput(attrs={
            'name':'title',
            'id':'title_id',
            'placeholder':'Title',
            'required':'required'
        })
    )
    content=forms.CharField(
        widget=Textarea(attrs={
            'name':'content',
            'id':'content_id',
            'required':'required'
        })
    )
    regions=tuple([tuple(i.name,) for i in Region.objects.all()])
    region=forms.ChoiceField(
        choices=regions,
        widget=ChoiceWidget(attrs={
            'name':'region',

        })
    )
    region_id=forms.CharField(
        widget=HiddenInput(attrs={
            'name':'region_id'
        })
    ) 
    

