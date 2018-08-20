from django import forms
from django.core.exceptions import ValidationError


class WriteOutForm(forms.Form):
    write_out = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 100}), label='Выписка')
    dispatcher = forms.CharField(label='Диспетчер', max_length=50)

    def clean_dispatcher(self):
        dispatcher = self.cleaned_data['dispatcher']
        if len(dispatcher) < 3:
            raise ValidationError('Too short')
        return dispatcher

    def clean(self):
        if self.cleaned_data.get('dispatcher', None) == 'Миша':
            raise ValidationError('No!')
        return self.cleaned_data

    def clean_write_out(self):
        if 'fuck' in self.cleaned_data.get('write_out', None):
            raise ValidationError('Fuck you')
        return self.cleaned_dat
