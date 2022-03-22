from django import forms

class SearchForm(forms.Form):
    adress = forms.CharField(max_length=50)

class AbusForm(forms.BaseForm):
    motif = forms.ChoiceField()