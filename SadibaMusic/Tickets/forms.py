from django import forms

class TextTicketForm(forms.Form):
    isRotated = forms.BooleanField()
    left = forms.FloatField()
    top = forms.FloatField()

class BarcodeForm(forms.Form):
    isRotated = forms.BooleanField()
    left = forms.FloatField()
    top = forms.FloatField()
    width = forms.FloatField()
    height = forms.FloatField()