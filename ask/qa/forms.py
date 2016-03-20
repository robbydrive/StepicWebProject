from django import forms
from qa.models import *

class AskForm(forms.Form):
	title = forms.CharField()
	text = forms.CharField(widget=forms.Textarea)
	
	def clean_title(self):
		title = self.cleaned_data['title']
		if len(title) < 1:
			raise ValidationError('Empty title')
		else:
			return title

	def clean_text(self):
		text = self.cleaned_data['text']
		if len(text) < 1:
			raise ValidationError('No text')
		else:
			return text

	def clean(self):
		if self.cleaned_data['title'] == self.cleaned_data['text']:
			raise ValidationError('Same title and text')
		
	def save(self):
		question = Question(**self.cleaned_data)
		question.save()
		return question

class AnswerForm(forms.Form):
	text = forms.CharField(widget=forms.Textarea)
	question = forms.CharField()

	def clean_text(self):
		text = self.cleaned_data['text']
		if len(text) < 1:
			raise ValidationError('No text')
		else:
			return text

	def clean_question(self):
		question = self.cleaned_data['question']
		try:
			question = int(question)
		except:
			raise ValidationError('Incorrect question id')
		return question

	def clean(self):
		if self.cleaned_data['text'] == str(self.cleaned_data['question']):
			raise ValidationError('Same answer and question text. You shouldn\'t waste our hard disk memory')
	
	def save(self):
		q = Question.objects.get(pk=question)
		answer = Answer(text=self.text, question=q)
		answer.save()
		return answer		
