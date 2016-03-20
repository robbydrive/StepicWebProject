from django import forms
from qa.models import *

class AskForm(forms.Form):
	title = forms.CharField()
	text = forms.CharField(widget=forms.Textarea)
	
	def clean(self):
		if self.cleaned_data['title'] == self.cleaned_data['text']:
			raise ValidationError('Same title and text')
		
	def save(self):
		question = Question()
		question.title = self.cleaned_data['title']
		question.text = self.cleaned_data['text']
		question.author= "Roman"
		question.save()
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
