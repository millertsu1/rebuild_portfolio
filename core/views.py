from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Projects

def home(request):
    return render(request, 'core/home.html') 

def portfolio(request):
    projects_list = Projects.objects.all()
    paginator = Paginator(projects_list, 3)  # Mostrar 3 proyectos por página
    page_number = request.GET.get('page')  # Obtener el número de la página actual
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'core/home.html', {'page_obj': page_obj})