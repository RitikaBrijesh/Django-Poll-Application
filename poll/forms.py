from dataclasses import field
from socket import fromshare
from turtle import textinput
from django.forms import ModelForm
from .models import PollQuestion
from django.forms import Textarea, TextInput

class PollForm(ModelForm):
    class Meta:
        model=PollQuestion
        fields=['username','question','first','second','third','fourth']

        widgets={
            'question':Textarea(attrs={
                'class':'form-control',
                'style': 'max-width: 300px;max-height:50px;\
                    margin-left:100px;',
                'placeholder':'Enter Poll Question'
            }),

            'first':TextInput(attrs={
                'class':'form-control',
                'style': 'max-width: 250px;max-height:35px;\
                    margin-left:120px;',
                'placeholder':'Option 1'
            }),

            'second':TextInput(attrs={
                'class':'form-control',
                'style': 'max-width: 250px;max-height:35px;\
                    margin-left:120px;',
                'placeholder':'Option 2'
            }),

            'third':TextInput(attrs={
                'class':'form-control',
                'style': 'max-width: 250px;max-height:35px;\
                    margin-left:120px;',
                'placeholder':'Option 3'
            }),

            'fourth':TextInput(attrs={
                'class':'form-control',
                'style': 'max-width: 250px;max-height:35px;\
                    margin-left:120px;',
                'placeholder':'Option 4'
            }),
        }
        