from django.shortcuts import redirect, render
from .models import Tareas, Pasos
from toDo_list.forms.Tareas import TareasForm as TareaForm
from toDo_list.forms.Pasos import PasosForm
# Create your views here.


def homePage(request):
    mydata = Tareas.objects.all()
    return render(request, 'tareas/index.html', {'mytask': mydata})


def nuevaTarea(request):
    if request.method == 'POST':
        formaTarea = TareaForm(request.POST)
        if formaTarea.is_valid():
            formaTarea.save()
            return redirect('/')
        else:
            print("El modelo no es valido")
    else:
        formaTarea = TareaForm()
    return render(request, 'tareas/nuevo.html', {'formaTarea':formaTarea})

def borrarTarea(request, id):
    
    tarea = Tareas.objects.get(pk=id)
    tarea.delete()
    
    return redirect('/')

def detalleTarea(request, id):
    tarea = Tareas.objects.get(pk=id)
    if request.method == 'POST':
        formaPasos = PasosForm(request.POST)
        if formaPasos.is_valid():
            formaPasos.save()
        else: 
            print("Aqui sucedio algo mal")
    else:
        formaPasos = PasosForm(initial={'tarea': tarea})
    pasos = Pasos.objects.filter(tarea=tarea.pk)
    return render(request, 'tareas/detalle.html', {'tarea':tarea, 'sinPasos':len(pasos) , 'pasos':pasos, 'pasosForm':formaPasos, 'pkTarea':id})
    
def completar_tarea(request, id):
    paso = Pasos.objects.get(pk=id)
                
    
    