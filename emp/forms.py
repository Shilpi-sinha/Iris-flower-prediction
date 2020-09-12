from django import forms
class EmployeeForm(forms.Form):
	s1=forms.FloatField()
	sw=forms.FloatField()
	p1=forms.FloatField()
	pw=forms.FloatField()