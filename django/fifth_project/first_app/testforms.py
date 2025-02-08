from django import forms

class Studentform(forms.Form):
    name= forms.CharField(label='User Name')
    email=forms.EmailField()
    Age= forms.CharField()
