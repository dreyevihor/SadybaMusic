from django import forms

class RowForm(forms.Form):
    row_from = forms.IntegerField()
    row_to = forms.IntegerField()
    place_from  = forms.IntegerField()
    place_to  = forms.IntegerField()
