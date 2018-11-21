from django import forms


class ArchiveForm(forms.Form):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)

    archive_from = forms.DateField(label='От',
                                   widget=forms.TextInput(attrs={'class': 'uk-input',
                                                                 'type': 'date'}))
    archive_to = forms.DateField(label='По',
                                 widget=forms.TextInput(attrs={'class': 'uk-input',
                                                               'type': 'date'}))
