from django import forms
from qa.models import *

class AskForm(forms.Form):
	title = forms.CharField()
	text = forms.CharField()

	def clean_title(self):
		title = self.cleaned_data['title']
		print self.cleaned_data, 'after clean_title'
		return title
	
	def clean_text(self):
		text = self.cleaned_data['text']
		print self.cleaned_data, 'after clean_text'
		return text
	
	def clean(self):
		if self.cleaned_data['title'] == self.cleaned_data['text']:
			raise ValidationError('Same title and text')
		print self.cleaned_data, 'after clean'
		
	def save(self):
		question = Question.objects.create()
		print self.cleaned_data, 'in save'
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
	
	def save(self):
		q = Question.objects.get(pk=int(self.cleaned_data['question']))
		answer = Answer()
		answer.text = self.cleaned_data['text']
		answer.question = q
		answet.author = "Romain"
		answer.save()
		return answer
