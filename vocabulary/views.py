from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from random import randint
from vocabulary.models import Word
import json

def index(request):
	return render(request, 'index.html')

def new(request):
#	return HttpResponse("Hello, world. You're at the polls index.")
	rand = randint(0, Word.objects.count()-1)
	prob = Word.objects.all()[rand].prob
	ans = Word.objects.all()[rand].ans

	return JsonResponse({'prob': prob, 'ans': ans})

def add(request):
	if request.method == 'POST':
		body_decode = request.body.decode('utf-8')
		body_data = json.loads(body_decode)
		Word.objects.create(prob = body_data['prob'], ans = body_data['ans'])
#		return HttpResponse
	return render(request, 'add.html')
