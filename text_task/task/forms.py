from django import forms


class TextFileForm(forms.Form):
    file = forms.FileField()
