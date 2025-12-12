from django import forms


class TitleForm(forms.Form):
    title = forms.CharField(label="Title", min_length=2, max_length=200, required=False)
