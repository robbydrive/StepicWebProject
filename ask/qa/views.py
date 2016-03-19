from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from qa.models import *

def test(request, *args, **kwargs):
	return HttpResponse('OK')

def main(request):
	limit = 10
	try:
		page = int(request.GET.get("page", 1))
	except ValueError:
		page = 1
	questions = Question.objects
	questions = questions.order_by("-added_at")
	paginator = Paginator(questions, limit)
	paginator.baseurl = "/?page="
	try:
		page = paginator.page(page)
	except EmptyPage:
		page = paginator.page(paginator.num_pages)
	return render(request, "main_page.html", {
		'questions': page.object_list,
		'paginator': paginator, 
		'page': page,
	})

def popular(request):
	limit = 10
	try:
		page = int(request.GET.get('page', 1))
	except ValueError:
		page = 1
	questions = Question.objects.order_by("-rating")
	paginator = Paginator(questions, limit)
	paginator.baseurl = "/popular/?page="
	try:
		page = paginator.page(page)
	except EmptyPage:
		page = paginator.page(paginator.num_pages)
	return render(request, "popular_page.html", {
		'questions': page.object_list,
		'paginator': paginator,
		'page': page,
	})

def question(request, question_id):
	try:
		question_id = int(question_id)
	except ValueError:
		raise Http404
	q = Question.objects.get(pk=question_id)
	answers = Answer.objects.all().filter(question = q)
	return render(request, "question_page.html", {
		'question': q,
		'answers': answers,
	})
