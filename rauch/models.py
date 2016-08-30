from __future__ import unicode_literals

from django.db import models

# Create your models here.


	
class Eigenschaft(models.Model):
	"""Repraesentiert eine Eigenschaft"""
	bezeichnung = models.CharField(max_length=200)
	
	def __str__(self):
		return self.bezeichnung
	
class Substanz(models.Model):
	"""Repraesentiert eine Substanz"""
	bezeichnung = models.CharField(max_length=200)
	name_botanisch = models.CharField(max_length=200)
	eigenschaften = models.ManyToManyField(Eigenschaft)
	kaufdatum = models.DateTimeField('Kaufdatum')
	preispergramm = models.IntegerField('Preis pro Gramm', default=0)	
	
	def __str__(self):
		return self.bezeichnung