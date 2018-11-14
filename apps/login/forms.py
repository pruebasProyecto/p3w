from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):
	class Meta:
		model = User
		fields = ("username","password1","password2")
		widgets = {
			"username": forms.TextInput(attrs={'class': 'input-field'}),
			"password1": forms.TextInput(attrs={'class': 'input-field'}),
			"password2": forms.TextInput(attrs={'class': 'input-field'}),
			}

		"""def save(self,commit=True):
			user = super(UserCreateForm,self).save(commit=False)
			if commit:
				user.save()
			return user"""
