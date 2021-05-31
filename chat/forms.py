from django import forms
from .models import *


class ChatForm(forms.ModelForm):

    class Meta:
        model = Chat
        fields = '__all__'

