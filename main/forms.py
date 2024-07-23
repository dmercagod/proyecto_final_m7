from django.forms import ModelForm
from main.models import Inmueble

class InmuebleForm(ModelForm):
  class Meta:
    model = Inmueble
    exclude = []