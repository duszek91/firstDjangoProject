from django import forms


class MathForm(forms.Form):
    x = forms.CharField()
    y = forms.CharField()
