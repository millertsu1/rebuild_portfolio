""" from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Projects,Experience

def home(request):
    return render(request, 'core/home.html') 

def portfolio(request):
    projects_list = Projects.objects.all()
    paginator = Paginator(projects_list, 3)  # Mostrar 3 proyectos por página
    page_number = request.GET.get('page')  # Obtener el número de la página actual
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'core/home.html', {'page_obj': page_obj})

def experience_list(request):
    experiences = Experience.objects.all().order_by('-start_date')
    context = {
        'experiences': experiences
    }
    return render(request, 'core/home.html', context) """

from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Projects, Experience, About

def home(request):
    # Obtener todos los proyectos y paginarlos
    projects_list = Projects.objects.all()
    paginator = Paginator(projects_list, 3)  # Mostrar 3 proyectos por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Obtener todas las experiencias laborales
    experiences = Experience.objects.all().order_by('-start_date')

    # Obtener todos los perfiles 
    abouts = About.objects.all()

    # Combinar los datos en el contexto
    context = {
        'page_obj': page_obj,
        'experiences': experiences,
        'abouts': abouts,
    }
    
    return render(request, 'core/home.html', context)
