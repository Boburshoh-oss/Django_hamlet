from django import forms 
from django.forms.widgets import ChoiceWidget, HiddenInput, TextInput, Textarea, NumberInput
from mysite.models import Region, District, Status, Property_type, locataion, Price, modum, imagae

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
    districts=tuple([tuple(i.name) for i in District.objects.all()])
    district=forms.ChoiceField(
        choices=districts,
        widget=ChoiceWidget(attrs={
            'name':'district'
        })
    )
    location=forms.CharField(
        widget=TextInput(attrs={
            'name':'location',
            'required':'required'
        })
    )
    types=tuple([tuple(i.name) for i in Property_type.objects.all()])
    Property_type=forms.CharField(
        choices=types,
        widget=ChoiceWidget(attrs={
            'name':'type',
            'required':'required'
        })
    )
    statses=tuple([tuple(i.name) for i in Status.objects.all()])
    Status=forms.CharField(
        choices=statses,
        widget=ChoiceWidget(attrs={
            'name':'status',
            'required':'required'
        })
    )
    price=forms.FloatField(
        widget=NumberInput(attrs={
            'name':'price',
            'required':'required'
        })
    )
    modum=forms.CharField(
        widget=Textarea(attrs={
            'name':'modum',
            'required':'required',
            'placeholder':'please provide information about the status of your ad'
        })
    )
    imagae=forms.ImageField() 
    phone=forms.IntegerField(
        widget=NumberInput(attrs={
            'name':'price',
            'required':'required'
        })
    )