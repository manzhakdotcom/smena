from django import forms
from django.core.exceptions import ValidationError


class WriteOutForm(forms.Form):
    write_out = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 100}), label='Выписка')
    dispatcher = forms.CharField(label='Диспетчер')

    def clean_dispatcher(self):
        dispatcher = self.cleaned_data['dispatcher']
        if len(dispatcher) < 5:
            raise ValidationError('Too short')
        return dispatcher

    def clean(self):
        if self.cleaned_data.get('dispatcher', None) == 'Миша':
            raise ValidationError('No!')
        return self.cleaned_data


