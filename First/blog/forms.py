from django import forms
from .models import Employee


class EmployeeForm(forms.Form):
    emp_name = forms.ChoiceField()
    emp_salary = forms.IntegerField()




