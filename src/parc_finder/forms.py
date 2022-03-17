from django import forms

class SearchForm(forms.Form):
    adress = forms.CharField(max_length=50)

