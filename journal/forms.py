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
    class Meta:
        model = WriteDown
        fields = ('date_created', 'write_down')
        widgets = {
            'date_created': forms.DateInput(attrs={'type': 'date'})
        }


class ExtraWriteOutForm(forms.ModelForm):
    class Meta:
        model = ExtraWriteOut
        fields = ('date_created', 'extra_write_out')
        widgets = {
            'date_created': forms.DateInput(attrs={'type': 'date'})
        }
