from django import forms
from journal.models import WriteOut, WriteDown, ExtraWriteOut


class WriteOutForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)

    write_down = forms.ModelChoiceField(queryset=WriteDown.objects.all(), widget=forms.HiddenInput)
    
    class Meta:
        model = WriteOut
        fields = ('write_down', 'date', 'time', 'text')
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'uk-input uk-form-width-medium uk-display-block'}),
            'time': forms.TimeInput(attrs={'type': 'time', 'class': 'uk-input uk-form-width-medium uk-display-block'}),
            'text': forms.Textarea(attrs={'class': 'uk-textarea'}),
        }


class WriteDownForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)

    class Meta:
        model = WriteDown
        fields = ('date', 'time', 'text')
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'uk-input uk-form-width-medium uk-display-block'}),
            'time': forms.TimeInput(attrs={'type': 'time', 'class': 'uk-input uk-form-width-medium uk-display-block'}),
            'text': forms.Textarea(attrs={'class': 'uk-textarea'}),
        }


class ExtraWriteOutForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)
    write_down = forms.ModelChoiceField(queryset=WriteDown.objects.all(), widget=forms.HiddenInput)
    
    class Meta:
        model = ExtraWriteOut
        fields = ('write_down', 'date', 'time', 'text')
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'uk-input uk-form-width-medium uk-display-block'}),
            'time': forms.TimeInput(attrs={'type': 'time', 'class': 'uk-input uk-form-width-medium uk-display-block'}),
            'text': forms.Textarea(attrs={'class': 'uk-textarea'}),
        }
