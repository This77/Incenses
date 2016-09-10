from django import forms
from .models import *

class SubstanzInputForm(forms.ModelForm):
    class Meta:
        model = Substanz
        fields = '__all__' #('bezeichnung',)
    """
    bezeichnung = forms.CharField(label='Bezeichnung', max_length=256)
    aka = forms.CharField(label='aka', max_length=1024)
    name_botanisch = forms.CharField(label='name_botanisch', max_length=256)
    herkunft = forms.CharField(label='herkunft', max_length=1024)
    tradition = forms.CharField(label='herkunft', max_length=2048)
    #kaufdatum = forms.DateTimeField('Kaufdatum', blank=True, null=True, default=None)
    preispergramm = forms.IntegerField(label='preisprogramm')
    """

class SubstanzInputSucheForm(forms.Form):
    bezeichnung = forms.CharField(label='Bezeichnung', max_length=256)

class EigenschaftInputForm(forms.ModelForm):
    class Meta:
        model = Eigenschaft
        fields = '__all__' #('bezeichnung',)
    """
    bezeichnung = forms.CharField(label='Bezeichnung', max_length=256)
    """

class EigenschaftInputSucheForm(forms.Form):
    bezeichnung = forms.CharField(label='Bezeichnung', max_length=256)