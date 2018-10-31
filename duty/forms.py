from django import forms

from staff.models import Employee, Workplace


class DutyForm(forms.Form):

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)

        workplaces = Workplace.objects.filter(organization__abbr='КТЦ')
        for workplace in workplaces:
            self.fields[str(workplace.id)] = forms.ModelChoiceField(
                queryset=Employee.objects.filter(organization__abbr='КТЦ'),
                label=str(workplace.name)
            )
            self.fields[str(workplace.id)].widget.attrs.update({
            'class': 'uk-select uk-form-width-medium uk-display-block'})

        workplaces = Workplace.objects.filter(organization__abbr='ЦУП')
        for workplace in workplaces:
            self.fields[str(workplace.id)] = forms.ModelChoiceField(
                queryset=Employee.objects.filter(organization__abbr='ЦУП'),
                label=str(workplace.name)
            )
            self.fields[str(workplace.id)].widget.attrs.update({
            'class': 'uk-select uk-form-width-medium uk-display-block'})
