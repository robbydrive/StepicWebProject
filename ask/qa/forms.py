from django import forms
from qa.models import *

class AskForm(forms.Form):
	title = forms.CharField()
	text = forms.CharField()

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
		#print self.cleaned_data, 'in save'
		#question.title = self.cleaned_data['title']
		#question.text = self.cleaned_data['text']
		#question.author= "Roman"
		#question.save()
		return question

class AnswerForm(forms.Form):
	text = forms.CharField(widget=forms.Textarea)
	question = forms.IntegerField()

	def clean(self):
		if self.cleaned_data['text'] == str(self.cleaned_data['question']):
			raise ValidationError('Same answer and question text. You shouldn\'t waste our hard disk memory')
		return self.cleaned_data
	
	def save(self):
		q = Question.objects.get(pk=int(self.cleaned_data['question']))
		answer = Answer()
		answer.text = self.cleaned_data['text']
		answer.question = q
		answet.author = "Romain"
		answer.save()
		return answer

class SignupForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField()
	email = forms.EmailField()

	def clean_username(self):
		return username
	
	def clean_password(self):
		return password
	
	def clean_email(self):
		return email

	def clean(self):
		return self.cleaned_data

	def save(self):
		user = User.objects.create_user(self.cleaned_data['username'], self.cleaned_data['password)'])
		user.email = self.cleaned_data(['email'])
		user.save()
		return user

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField()

	def clean_username(self):
		return username

	def clean_password(self):
		return password

	def clean(self):
		return self.cleaned_data

	def save(self):
		user = authenticate(username = self.cleaned_data['username'], password = self.cleaned_data['password'])
		if user:
			return user
		else:
			raise ValidationError('invalid username/password')
