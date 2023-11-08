from django import forms

from schedule.models import Student


class SearchForm(forms.Form):
    q = forms.CharField()


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
