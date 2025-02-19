from django import forms

class Studentform(forms.Form):
    name= forms.CharField(label='User Name')
    email=forms.EmailField()
    Age= forms.IntegerField()
    Weight=forms.FloatField()
    Date=forms.DateField()
    Choice=[('S','Small'),('M','Medium'),('L', 'Large')]
    Size=forms.ChoiceField(choices=Choice)
    Check=forms.BooleanField()
    
    
