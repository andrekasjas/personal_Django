from django.shortcuts import render
from Proyectos.models import proyectos, categorias, tecnologias
from django.db.models import Q
# Create your views here.



def cantidad():
    categoris = []
    tecnologis = []
    categoriss = categorias.objects.all()
    tecnologiss = tecnologias.objects.all()
    proyects = proyectos.objects.all()


    for cate in categoriss:
        cc = 0
        for proyec in proyects:
            if cate == proyec.categoria:
                cc += 1
        categoris.append({'id':cate.id,
                        'nombre':cate.nombre,
                        'cantidad':cc})

    for tecnolo in tecnologiss:
        cc = 0
        for proyec in proyects:
            for proy in proyec.tecnologia.all():
                if tecnolo == proy:
                    cc += 1
        tecnologis.append({'id':tecnolo.id,
                        'nombre':tecnolo.nombre,
                        'cantidad':cc})
    return categoris, tecnologis

def buscar(queryset):
    mensaje = False
    proyects = proyectos.objects.filter(
        Q(nombre__icontains = queryset) |
        Q(categoria__nombre__icontains = queryset) |
        Q(tecnologia__nombre__icontains = queryset) 
    ).distinct()
    if (queryset == 'todos') | (queryset == 'todo'):
        proyects = proyectos.objects.all().order_by('-created')
    elif not proyects:
        mensaje = queryset
    return mensaje, proyects

def proyectoss(request):
    
    categoris,tecnologis = cantidad()
    proyects = proyectos.objects.all().order_by('-created')
    proyects = proyects
    queryset = request.POST.get("buscar")
    mensaje = False
    if queryset:
        mensaje, proyects = buscar(queryset)
    return render(request,'Proyectos/proyectos.html',{'proyects': proyects, 
                                                        "categoris":categoris, 
                                                        "tecnologis":tecnologis,
                                                        "mensaje":mensaje})

def categoria(request, categoria_id):
    categoris,tecnologis = cantidad()
    categori = categorias.objects.get(id = categoria_id)
    proyects = proyectos.objects.filter(categoria = categoria_id).order_by('-created')
    queryset = request.POST.get("buscar")
    mensaje = False
    if queryset:
        mensaje, proyects = buscar(queryset)
    return render(request, 'Proyectos/categoria.html', {"categori":categori, 
                                                        "categoris":categoris,
                                                        "proyects":proyects, 
                                                        "tecnologis":tecnologis,
                                                        "mensaje":mensaje})

def tecnologia(request, tecnologia_id):
    categoris,tecnologis = cantidad()
    tecnologi = tecnologias.objects.get(id = tecnologia_id)
    proyects = proyectos.objects.filter(tecnologia = tecnologia_id).order_by('-created')
    queryset = request.POST.get("buscar")
    mensaje = False
    if queryset:
        mensaje, proyects = buscar(queryset)
    return render(request, 'Proyectos/tecnologia.html', {"tecnologi":tecnologi, 
                                                        "categoris":categoris,
                                                        "proyects":proyects, 
                                                        "tecnologis":tecnologis,
                                                        "mensaje":mensaje})

