from django import forms

from station.models import Circle
from staff.models import Employee


class DutyForm(forms.Form):

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(DutyForm, self).__init__(*args, **kwargs)

        self.fields['circle_0'] = forms.ModelChoiceField(queryset=Employee.objects.filter(organization__abbr='КТЦ'), label='Дежурный инженер КТЦ')
        self.fields['circle_0'].widget.attrs.update({
            'class': 'uk-select uk-form-width-medium uk-display-block'})

        circles = Circle.objects.all()
        for circle in circles:
            self.fields['circle_%s' % circle.id] = forms.ModelChoiceField(queryset=Employee.objects.filter(organization__abbr='ЦУП'), label='Диспетчер (' + str(circle.name) + ')')
            self.fields['circle_%s' % circle.id].widget.attrs.update({
            'class': 'uk-select uk-form-width-medium uk-display-block'})
