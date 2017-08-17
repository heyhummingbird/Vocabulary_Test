from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from random import randint
from vocabulary.models import Word
import json

def index(request):
	return render(request, 'index.html')

def new(request):
	rand = randint(0, Word.objects.count()-1)
	prob = Word.objects.all()[rand].prob
	ans = Word.objects.all()[rand].ans
	return JsonResponse({'prob': prob, 'ans': ans})

def add(request):
	return render(request, 'add.html')

def data(request):
	if request.method == 'POST':
		body_decode = request.body.decode('utf-8')
		body_data = json.loads(body_decode)
		Word.objects.create(prob = body_data['prob'], ans = body_data['ans'])
		return HttpResponse()
	elif request.method == 'DELETE':
		body_decode = request.body.decode('utf-8')
		body_data = json.loads(body_decode)
		Word.objects.filter(id=body_data['word_id']).delete()
		return HttpResponse()
	return HttpResponse(status=500)
	

def show_problemset(request):
	return render(request, 'show.html', {
		'words': Word.objects.all(),
		'num': Word.objects.count()
	})
