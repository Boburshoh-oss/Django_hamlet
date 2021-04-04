from django import forms
from .models import Post,Comment
from django.forms.widgets import TextInput, EmailInput, Textarea, FileInput
from django.contrib.auth.models import User


class CommentForm(forms.ModelForm):
    body = forms.CharField(widget = Textarea(attrs={
            'class':'form-control',
            'id':'message',
            'cols':'30',
            'rows':'10'
        }))
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
        
        # widgets = {
        #     'name':forms.TextInput(attrs={'class':'form-control'}),
        #     'email':forms.EmailInput(attrs={'class':'form-control'}),
        #     'body':forms.Textarea(attrs={'class':'form-control'}),
        # }

# class CommentForm(forms.ModelForm):
#     content=forms.CharField(widget=forms.Textarea(attrs={
#         'rows':'4'
#     }), required=False)
#     class Meta:
#         model=Comment
#         fields=('content',)
#         db_table = 'Commentary'
#         managed = True
#         verbose_name = 'Comment'
#         verbose_name_plural = 'Comments'

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'tags',
        ]