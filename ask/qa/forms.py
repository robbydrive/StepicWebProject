from django import forms
from qa.models import *
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class AskForm(forms.Form):
	title = forms.CharField()
	text = forms.CharField()
	_user = User()

	def clean_title(self):
		title = self.cleaned_data['title']
		#print self.cleaned_data, 'after clean_title'
		return title
	
	def clean_text(self):
		text = self.cleaned_data['text']
		#print self.cleaned_data, 'after clean_text'
		return text
	
	def clean(self):
		if self.cleaned_data['title'] == self.cleaned_data['text']:
			raise ValidationError('Same title and text')
		#print self.cleaned_data, 'after clean'
		return self.cleaned_data
		
	def save(self):
		question = Question.objects.create(**self.cleaned_data)
		print self._user, 'in ask form'
		print self._user.is_anonymous(), 'anonymous in ask form'
		#print self.cleaned_data, 'in save'
		#question.title = self.cleaned_data['title']
		#question.text = self.cleaned_data['text']
		if (self._user is not None) and (self._user.is_anonymous() == False):
			question.author = self._user
		#else:
		#	question.author = User(username="")
		question.save()
		return question

class AnswerForm(forms.Form):
	text = forms.CharField(widget=forms.Textarea)
	question = forms.IntegerField()
	_user = User()

	def clean(self):
		if self.cleaned_data['text'] == str(self.cleaned_data['question']):
			raise ValidationError('Same answer and question text. You shouldn\'t waste our hard disk memory')
		return self.cleaned_data
	
	def save(self):
		q = Question.objects.get(pk=int(self.cleaned_data['question']))
		answer = Answer()
		answer.text = self.cleaned_data['text']
		answer.question = q
		print self._user, 'in answer form'
		if self._user is not None and self._user.is_anonymous() == False:
			answer.author = self._user
		#else:
		#	answer.author = "Anonymous user"
		answer.save()
		return answer

class SignupForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField()
	email = forms.EmailField()

	def clean_username(self):
		return self.cleaned_data['username']
	
	def clean_password(self):
		return self.cleaned_data['password'] 
	
	def clean_email(self):
		return self.cleaned_data['email'] 

	def clean(self):
		return self.cleaned_data

	def save(self):
		user = User.objects.create_user(self.cleaned_data['username'], self.cleaned_data['password'])
		user.email = self.cleaned_data['email']
		user.set_password(self.cleaned_data['password'])
		user.save()
		return user

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField()

	def clean_username(self):
		return self.cleaned_data['username']

	def clean_password(self):
		return self.cleaned_data['password']

	def clean(self):
		return self.cleaned_data

	def save(self):
		user = authenticate(username = self.cleaned_data['username'], password = self.cleaned_data['password'])
		if user:
			return user
		else:
			raise ValidationError('invalid username/password')
