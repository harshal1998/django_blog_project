from django import forms
from django.forms import ModelForm

from .models import *


class bform(forms.ModelForm):
    class Meta:
        model = blog
        fields = "__all__"


# class chform(forms.ModelForm):
#     data = blog.objects.only('name')
#     names = []
#     for i in data:
#         a = (str(i), str(i))
#         names.append(a)
#     names = tuple(names)
#     name = forms.ChoiceField(choices=names)
#
#     class Meta:
#         model = blog
#         fields = ['name']

#
# class chform(forms.ModelForm):
#     class Meta:
#         model = ch
#         fields = ['name']
