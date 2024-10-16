from django import forms


class TextFileForm(forms.Form):
    file = forms.FileField()

    def __init__(self, *args, **kwargs) -> None:
        super(TextFileForm, self).__init__(*args, **kwargs)

        self.fields["file"].label = "Only .txt file"
