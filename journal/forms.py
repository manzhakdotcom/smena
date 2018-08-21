from django import forms
from journal.models import WriteOut, WriteDown


class WriteOutForm(forms.ModelForm):
    class Meta:
        model = WriteOut
        fields = ('date_created', 'write_out')


class WriteDownForm(forms.ModelForm):
    class Meta:
        model = WriteDown
        fields = ('date_created', 'write_down')