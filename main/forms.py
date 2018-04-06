# -*- coding: utf-8 -*-
from django import forms
from django.core.exceptions import ValidationError

class ContactsForm(forms.Form):
	name = forms.CharField(label='Введите имя', widget=forms.TextInput)
	phone = forms.CharField(label='Введите номер телефона', max_length=20)

	# clean_<fieldname> validation
	def clean_phone(self):
		data = self.cleaned_data['phone']

		# Проверка на наличие букв 
		if data.isalpha():
			raise ValidationError('Номер телефона не должен содержать букв')

		return data
