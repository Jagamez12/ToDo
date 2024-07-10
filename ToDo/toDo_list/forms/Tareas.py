from django.forms import DateTimeInput, ModelForm, TextInput
from toDo_list.models import Tareas

class TareasForm(ModelForm):
    class Meta:
        model = Tareas
        fields = ["titulo", "fechaFinalizacion"]
        widgets = {
            "titulo": TextInput(attrs={"class": "form-control"}),
            "fechaFinalizacion": DateTimeInput(attrs={"class":"form-control", "type":"date"})
        }