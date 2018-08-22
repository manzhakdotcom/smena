from django import forms
from journal.models import WriteOut, WriteDown, ExtraWriteOut


class WriteOutForm(forms.ModelForm):
    class Meta:
        model = WriteOut
        fields = ('date_created', 'write_out')
        widgets = {
            'date_created': forms.DateInput(attrs={'type': 'date'})
        }


class WriteDownForm(forms.ModelForm):
    class Meta:
        model = WriteDown
        fields = '__all__'
        widgets = {
            'date_created': forms.DateInput(attrs={'type': 'date'})
        }


class ExtraWriteOutForm(forms.ModelForm):
    class Meta:
        model = ExtraWriteOut
        fields = '__all__'
        widgets = {
            'date_created': forms.DateInput(attrs={'type': 'date'})
        }
