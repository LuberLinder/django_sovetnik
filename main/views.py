# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .forms import ContactsForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

def index(request):
	return render(request, 'main/index.html')

def about(request):
	return render(request, 'main/about.html')

def galary(request):
	return render(request, 'main/galary.html')

def news(request):
	return render(request, 'main/news.html')

def contacts(request):
	#return render(request, 'main/contacts.html')

	#def get_name(request):
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = ContactsForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			subject = 'Order'
			sender = 'my@mail.com'
			name = form.cleaned_data['name']
			phone = form.cleaned_data['phone']

			message = ' Name: ' + str(name) + ' Phone: ' + str(phone)
			recipients = ['luberlinder@gmail.com']

			send_mail(subject, message, sender, recipients)

			return HttpResponseRedirect('/thanks/')

	# if a GET (or any other method) we'll create a blank form
	else:
		form = ContactsForm()

	return render(request, 'main/contacts.html', {'form': form})

def thanks(request):
	return render(request, 'main/thanks.html')
