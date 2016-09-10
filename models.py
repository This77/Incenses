from __future__ import unicode_literals
from django.db import models


class Eigenschaft(models.Model):
    """Repraesentiert eine Eigenschaft"""
    bezeichnung = models.CharField(max_length=256)

    def __str__(self):
        return '{0}({1})'.format(self.bezeichnung, str(self.id))

class Substanz(models.Model):
    """Repraesentiert eine Substanz"""
    bezeichnung = models.CharField(max_length=256)
    aka = models.CharField(max_length=1024, blank=True, null=True)
    name_botanisch = models.CharField(max_length=256)
    herkunft = models.CharField(max_length=1024, blank=True, null=True)
    tradition = models.CharField(max_length=2048, blank=True, null=True)
    eigenschaft_set = models.ManyToManyField(Eigenschaft)
    #kaufdatum = models.DateTimeField('Kaufdatum', blank=True, null=True, default=None)
    preispergramm = models.IntegerField('Preis pro Gramm', default=0)

    def __str__(self):
        return '{0}({1})'.format(self.bezeichnung, str(self.id))