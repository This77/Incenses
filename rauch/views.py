from django.shortcuts import render
from django.http import HttpResponse

from .models import Substanz, Eigenschaft


def index(request):
	return HttpResponse("Hello This. You're at the index of Rauch.")
	
def substanz_liste(request):
	return HttpResponse("Hier ist die Liste.")
	
def substanz_singleform(request, substanz_id):
	substanz = Substanz.objects.get(id=substanz_id)
	eigenschaften = substanz.eigenschaften.all()
	response = ["Du schaust die Substanz %s (id=%s) an." %(substanz.bezeichnung, str(substanz_id))]
	response.append("Ihre Eigenschaften sind:")
	for e in eigenschaften:
		response.append("- %s" %e.bezeichnung)
	response = r'<br>'.join(response)
	return HttpResponse(response)
	
def substanz_images(request, substanz_id):
	response = "Du schaust die Fotos der Substanz %s an."
	return HttpResponse(response %str(substanz_id))	
	
def verzeichnis(request):
	return HttpResponse('Hier kommt das Verzeichnis hin.')

# Create your views here.
