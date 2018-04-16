#-*- coding: utf-8 -*-
from django import forms

class LoginForm(forms.Form):
   title = forms.CharField(max_length = 100)
   # description = forms.TextField(max_length=50)