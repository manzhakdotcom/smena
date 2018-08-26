from django import forms
from journal.models import WriteOut, WriteDown, ExtraWriteOut


class WriteOutForm(forms.ModelForm):
    write_down = forms.ModelChoiceField(queryset=WriteDown.objects.all(), widget=forms.HiddenInput)

    class Meta:
        model = WriteOut
        fields = ('date_created', 'write_out', 'write_down')
        widgets = {
            'date_created': forms.DateInput(attrs={'type': 'date'})
        }


class WriteDownForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(WriteDownForm, self).__init__(*args, **kwargs)

    class Meta:
        model = WriteDown
        fields = ('date_created', 'write_down')
        widgets = {
            'date_created': forms.DateInput(attrs={'type': 'date', 'class': 'uk-input uk-form-width-medium uk-display-block'}),
            'write_down': forms.Textarea(attrs={'class': 'uk-textarea'}),
        }


class ExtraWriteOutForm(forms.ModelForm):
    class Meta:
        model = ExtraWriteOut
        fields = ('date_created', 'extra_write_out')
        widgets = {
            'date_created': forms.DateInput(attrs={'type': 'date'})
        }
