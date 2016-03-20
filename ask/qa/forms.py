from django import forms
from models import Question

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
	question = Question()

	def clean_text(self):
		text = self.cleaned_data['text']
		if len(text) < 1:
			raise ValidationError('No text')
		else:
			return text

	def clean(self):
		if self.cleaned_data['text'] == self.cleaned_data['question'].title:
			raise ValidationError('Same answer and question text. You shouldn\'t waste our hard disk memory')
	
	def save(self):
		answer = Answer(**self.cleaned_data)
		answer.save()
		return answer		
