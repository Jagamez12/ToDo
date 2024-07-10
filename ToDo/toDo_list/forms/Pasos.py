from django.forms import DateTimeInput, ModelForm, TextInput, HiddenInput
from toDo_list.models import Pasos


class PasosForm(ModelForm):
    class Meta:
        model = Pasos
        fields = ['titulo', 'descripcion', 'tarea']
        widgets = {
            'titulo': TextInput(attrs={'class':'form-control'}),
            'descripcion': TextInput(attrs={'class':'form-control'}),
            'tarea': HiddenInput()
        }