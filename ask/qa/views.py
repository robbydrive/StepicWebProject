from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from qa.models import *
from django.views.decorators.csrf import csrf_exempt
from qa.forms import *
from django.contrib.auth import authenticate, login

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
@csrf_exempt
def question(request, question_id):
	try:
		question_id = int(question_id)
	except ValueError:
		raise Http404
	q = Question.objects.get(pk=question_id)
	answers = Answer.objects.all().filter(question = q)
	form = AnswerForm()
	return render(request, "question_page.html", {
		'question': q,
		'answers': answers,
		'form': form
	})

@csrf_exempt
def ask(request):
	if request.method == "POST":
		form = AskForm(request.POST)
		form._user = request.user
		if form.is_valid():
			#print form.cleaned_data, 'before form.save()'
			question = form.save()
			url = "/question/" + str(question.id) + "/"
			return HttpResponseRedirect(url)
	else:
		form = AskForm()
	return render(request, 'ask_form.html', {
		'form': form
	})
@csrf_exempt
def answer(request):
	if request.method == "POST":
		form = AnswerForm(request.POST)
		form._user = request.user
		if form.is_valid():
			answer = form.save()
			url = "/question/" + answer.question.id + "/"
			return HttpResponseRedirect(url)

@csrf_exempt
def signup(request):
	if request.method == "POST":
		form = SignupForm(request.POST)
		if form.is_valid():
			user = form.save()
			user = authenticate(username = user.username, password = request.POST['password'])
			login(request, user)
			return HttpResponseRedirect('/')
	else:
		form = SignupForm()
	return render(request, 'signup.html', {'form': form})

@csrf_exempt
def log_in(request):
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			user = form.save()
			if user:
				login(request, user)
				return HttpResponseRedirect('/')
	else:
		form = LoginForm()
	return render(request, 'login.html', {'form': form})

