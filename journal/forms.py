from django import forms
from journal.models import WriteOut, WriteDown, ExtraWriteOut


class WriteOutForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(WriteOutForm, self).__init__(*args, **kwargs)

    class Meta:
        model = WriteOut
        fields = ('date_created', 'text')
        widgets = {
            'date_created': forms.DateInput(attrs={'type': 'date', 'class': 'uk-input uk-form-width-medium uk-display-block'}),
            'text': forms.Textarea(attrs={'class': 'uk-textarea'}),
        }


class WriteDownForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(WriteDownForm, self).__init__(*args, **kwargs)

    class Meta:
        model = WriteDown
        fields = ('date_created', 'text')
        widgets = {
            'date_created': forms.DateInput(attrs={'type': 'date', 'class': 'uk-input uk-form-width-medium uk-display-block'}),
            'text': forms.Textarea(attrs={'class': 'uk-textarea'}),
        }


class ExtraWriteOutForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(ExtraWriteOutForm, self).__init__(*args, **kwargs)

    class Meta:
        model = ExtraWriteOut
        fields = ('date_created', 'text')
        widgets = {
            'date_created': forms.DateInput(attrs={'type': 'date', 'class': 'uk-input uk-form-width-medium uk-display-block'}),
            'text': forms.Textarea(attrs={'class': 'uk-textarea'}),
        }
