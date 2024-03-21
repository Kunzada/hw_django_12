# from django.forms import forms
from django import forms
from .models import *
# class SearchForm(forms.Form):
#     search = forms.CharField(label='Search', max_length=100)


class EmployeesForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields=['firstName','lastName','email','phoneNumber','salary']
        # wedgets = {
        #     'first_name': forms.CharField(attrs={'class': 'form-control'}),
        #     'last_name': forms.CharField(attrs={'class': 'form-control'}),
        #     'email': forms.CharField(attrs={'class': 'form-control'}),
        #     'phoneNumber': forms.CharField(attrs={'class': 'form-control'}),
        #     'salary': forms.IntegerField(attrs={'class': 'form-control'}),
        # }

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['image','jobTitle','minSalary','maxSalary','employees','startDate','endDate']

class TaskForm(forms.ModelForm):
    class Meta:
        model =Task 
        fields=['title','description','job']
    