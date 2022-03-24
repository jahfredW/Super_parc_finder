from django import forms
from parc.models import Location

class SearchForm(forms.Form):
    adress = forms.CharField(max_length=50)


class AbusForm(forms.BaseForm):
    motif = forms.ChoiceField()


class ParcCreateForm(forms.ModelForm):

    class Meta:
        model = Location
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ParcCreateForm, self).__init__(*args, **kwargs)


