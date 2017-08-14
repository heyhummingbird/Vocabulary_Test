from django.db import models

class Word(models.Model):
	prob = models.TextField(default='')
	ans = models.TextField(default='')
