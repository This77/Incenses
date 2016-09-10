from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Substanz, Eigenschaft
from .forms import *

def index(request):
    return HttpResponse("Hello This. You're at the index of Rauch.")

def verzeichnis(request):
    return HttpResponse('Hier kommt das Verzeichnis hin.')

def substanz_input(request):
    #template = loader.get_template('rauch/substanz_input.html')
    #context = {'substanz_input': substanz_input,}
    #return HttpResponse(template.render(context, request))

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # We save the data
        if 'save' in request.POST:
            # create a form instance and populate it with data from the request:
            form_input = SubstanzInputForm(request.POST)
            # Wanna sniff?
            #print request.META
            # check whether it's valid:
            if form_input.is_valid():
                try:
                    bezeichnung = form_input.cleaned_data['bezeichnung']
                    substanz = Substanz.objects.get(bezeichnung=bezeichnung)
                except Substanz.DoesNotExist:
                    # Create new object.
                    substanz = Substanz()
                # Populate object
                for k, v in form_input.cleaned_data.iteritems():
                        if hasattr(substanz, k):
                            setattr(substanz, k, v)
                substanz.save()
                # Redirect to substanz_singleform
                return redirect('rauch:substanz_singleform', substanz_id=substanz.id)
            else:
                # Data invalid
                return HttpResponseRedirect('/input_invalid/')
        elif 'search' in request.POST:
            s = Substanz.objects.get(id=1)
            # create a form instance and populate it with data from the request:
            form_search = SubstanzInputSucheForm(initial={'bezeichnung':s.bezeichnung})
            form_input = SubstanzInputForm(instance=s)
            return render(request, 'rauch/substanz_input.html', {'form_input': form_input, 'form_search':form_search})
        else:
            # Request invalid
            return HttpResponseRedirect('/request_invalid/')
    # if a GET (or any other method) we'll create a blank form
    else:
        # Show native
        form_input = SubstanzInputForm()
        form_search = SubstanzInputSucheForm()
        return render(request, 'rauch/substanz_input.html', {'form_input': form_input, 'form_search':form_search})

def substanz_liste(request):
    substanz_liste = Substanz.objects.order_by('bezeichnung')
    return render(request, 'rauch/substanz_liste.html', {'substanz_liste':substanz_liste})

def substanz_singleform(request, substanz_id):
    """Most imortant view.
    Therefore I try to code "oldschool" without helpers.
    SO I can learn the concepts behind them.
    Other functions may use helpers."""
    # Errorhandling can be done with django.shortcuts.get_object_or_404().
    # This would then be considered "controlled coupling of view layer and model layer".
    try:
        substanz = Substanz.objects.get(id=substanz_id)
    except Substanz.DoesNotExist:
        raise Http404('Substanz not found.')
    eigenschaft_liste = substanz.eigenschaft_set.order_by('bezeichnung')
    # Use shortcut "renderer" to simplify the common idiom:
    # Load template
    # Fill context into template
    # Render the filled temlate
    # Return HTTPResponse with the result of the rendering
    return render(request, 'rauch/substanz_singleform.html', {'substanz':substanz, 'eigenschaft_liste':eigenschaft_liste})

def substanz_images(request, substanz_id):
    response = "Du schaust die Fotos der Substanz %s an."
    return HttpResponse(response %str(substanz_id))

def eigenschaft_input(request):
    #template = loader.get_template('rauch/substanz_input.html')
    #context = {'substanz_input': substanz_input,}
    #return HttpResponse(template.render(context, request))

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # We save the data
        if 'save' in request.POST:
            # create a form instance and populate it with data from the request:
            form_input = EigenschaftInputForm(request.POST)
            # Wanna sniff?
            #print request.META
            # check whether it's valid:
            if form_input.is_valid():
                try:
                    bezeichnung = form_input.cleaned_data['bezeichnung']
                    eigenschaft = Eigenschaft.objects.get(bezeichnung=bezeichnung)
                except Eigenschaft.DoesNotExist:
                    # Create new object.
                    eigenschaft = Eigenschaft()
                # Populate object
                for k, v in form_input.cleaned_data.iteritems():
                        if hasattr(eigenschaft, k):
                            setattr(eigenschaft, k, v)
                eigenschaft.save()
                # Redirect to substanz_singleform
                return redirect('rauch:eigenschaft_singleform', eigenschaft_id=eigenschaft.id)
            else:
                # Data invalid
                return HttpResponseRedirect('/input_invalid/')
        elif 'search' in request.POST:
            e = Eigenschaft.objects.get(id=1)
            # create a form instance and populate it with data from the request:
            form_search = EigenschaftInputSucheForm(initial={'bezeichnung':e.bezeichnung})
            form_input = EigenschaftInputForm(instance=e)
            return render(request, 'rauch/eigenschaft_input.html', {'form_input': form_input, 'form_search':form_search})
        else:
            # Request invalid
            return HttpResponseRedirect('/request_invalid/')
    # if a GET (or any other method) we'll create a blank form
    else:
        # Show native
        form_input = EigenschaftInputForm()
        form_search = EigenschaftInputSucheForm()
        return render(request, 'rauch/eigenschaft_input.html', {'form_input': form_input, 'form_search':form_search})

def eigenschaft_liste(request):
    eigenschaft_liste = Eigenschaft.objects.order_by('bezeichnung')
    return render(request, 'rauch/eigenschaft_liste.html', {'eigenschaft_liste':eigenschaft_liste})

def eigenschaft_singleform(request, eigenschaft_id):
    eigenschaft = get_object_or_404(Eigenschaft, id=eigenschaft_id)
    substanz_liste = eigenschaft.substanz_set.order_by('bezeichnung')
    return render(request, 'rauch/eigenschaft_singleform.html', {'eigenschaft':eigenschaft, 'substanz_liste':substanz_liste})

# Create your views here.
