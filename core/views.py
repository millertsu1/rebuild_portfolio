from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Projects, Experience, About

def home(request):
    # Obtener todos los proyectos y paginarlos
    projects_list = Projects.objects.all()
    paginator = Paginator(projects_list, 6)  # Mostrar 3 proyectos por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Obtener todas las experiencias laborales
    experiences = Experience.objects.all().order_by('-start_date')

     # Obtener el perfil activo de About
    active_about = About.objects.filter(active=True).first()

    # Combinar los datos en el contexto
    context = {
        'page_obj': page_obj,
        'experiences': experiences,
        'active_about': active_about, 
    }
    
    return render(request, 'core/home.html', context)