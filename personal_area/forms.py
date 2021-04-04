from django import forms 
from django.forms.widgets import ChoiceWidget, HiddenInput, TextInput, Textarea, NumberInput
from mysite.models import *
from django import forms



# class UpdateAddForm(forms.ModelForm):
    
#     class Meta:
#         model = Announcement
#         fields = ['title','region','district','location','Beds','Bathroom','Property_type','status','Agents','modum','image','Price','phone','Garage']
#         widgets = {
#             'title':forms.TextInput(attrs={'class':'form-control h6'}),
#             'region':forms.Select(attrs={'class':'form-control'}),
#             'district':forms.Select(attrs={'class':'form-control'}),
#             'Property_type':forms.Select(attrs={'class':'form-control'}),
#             'status':forms.Select(attrs={'class':'form-control'}),          
#             'image':forms.FileInput(attrs={'class':'form-control'}),
#             'location':forms.TextInput(attrs={'class':'form-control'}),
#             'Agents':forms.TextInput(attrs={'class':'form-control'}),
#             'Beds':forms.NumberInput(attrs={'class':'form-control'}),
#             'Bathroom':forms.NumberInput(attrs={'class':'form-control'}),
#             'Phone':forms.NumberInput(attrs={'class':'form-control'}),
#             'Garage':forms.NumberInput(attrs={'class':'form-control'}),
#             'modum':forms.Textarea(attrs={'class':'form-control'}),
#             'Price':forms.Select(attrs={'class':'form-control'}),

#         }
"""class Filter(forms.Form):
    types=(
       
        ('Commericial','Commerical'),
        ('-Office','-Office'),
        ('Residential','Residential')
        ('Villa','Villa'),
        ('Condominium','Condominium'),
        ('Apartment','Apartment')
    )
    sts=[
        ('Rent','Rent'),
        ('Sale','Sale')
    ]
    limit=['5000','10000','50000','100000','200000','300000','400000','500000','600000','700000','800000','900000','1000000','2000000']
    location=forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'City/Locality Name',
                'name':'keyvalue',
                'type':'text'
            }
        )
    )
    Property_type=forms.MultipleChoiceField(
        required=False,
        choices=types,
        widget=forms.CheckboxSelectMultiple(
            attrs={
                'class':'form-control',
                'placeholder':'Propert Type',
                'name':'Property_id',
                'type':'text'
            }
        )
        
    )
    Property_status=forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple(
            attrs={
                'class':'form-control',
                'placeholder':'Propert Status',
                'name':'status_id',
                'type':'text'
            }
        )
        choices=sts
    )
    Price_limit=forms.DateInput(
        widget=forms.NumberInput(attrs={
            'class':'form-control',
            'placeholder':'Price Limit',
            'name':'Price Limit',

        })
    ) #DateField(widget=forms.SelectDateWidget(years=limit))"""

class ImgForm(forms.ModelForm): 
  
    class Meta: 
        model = Announcement 
        fields = ['title', 'location','author','image','Agents','Beds','Bathroom','Property_type','Price','status','phone','modum']
    """def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['district'].queryset = District.objects.none()

        if 'region' in self.data:
            try:
                region_id = int(self.data.get('region'))
                self.fields['district'].queryset = District.objects.filter(region_id=region_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['district'].queryset = self.instance.country.city_set.order_by('name')"""
"""class AddForm(forms.Form):
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
    )"""
