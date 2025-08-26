from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Casa, Opinion, Promocion
from .forms import CasaForm, OpinionForm, PromocionForm

# 🔹 Verificación de usuario administrador
def es_admin(user):
    return user.is_authenticated and (user.is_staff or user.is_superuser)

# 🔹 Vista para ver TODAS las opiniones
def todas_opiniones(request):
    opiniones = Opinion.objects.all().order_by('-fecha_creacion')
    return render(request, 'inicio/ver_opiniones.html', {'opiniones': opiniones})

# 🔹 Lista de casas (solo publicadas para usuarios normales)
def lista_casas(request):
    casas = Casa.objects.filter(publicado=True)
    return render(request, 'inicio/lista_casas.html', {'casas': casas})

# 🔹 Detalles de la casa + opiniones
def detalles_casa(request, pk):
    casa = get_object_or_404(Casa, pk=pk)
    opiniones = casa.opiniones.order_by('-fecha_creacion')

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = OpinionForm(request.POST)
            if form.is_valid():
                opinion = form.save(commit=False)
                opinion.usuario = request.user
                opinion.casa = casa
                opinion.save()
                messages.success(request, "¡Tu opinión se ha registrado! 📝")
                return redirect('casas:detalles_casa', pk=casa.id)
        else:
            messages.error(request, "Debes iniciar sesión para dejar una opinión.")
            return redirect('login')
    else:
        form = OpinionForm()

    return render(request, 'inicio/detalles_casa.html', {
        'casa': casa,
        'opiniones': opiniones,
        'form': form
    })

# ==============================
# CRUD DE CASAS — SOLO ADMIN
# ==============================

@login_required
@user_passes_test(es_admin)
def admin_lista_casas(request):
    casas = Casa.objects.all()
    return render(request, 'inicio/admin_lista_casas.html', {'casas': casas})

@login_required
def crear_casa(request):
    if request.method == "POST":
        form = CasaForm(request.POST, request.FILES)
        if form.is_valid():
            casa = form.save(commit=False)
            casa.propietario = request.user
            casa.save()
            messages.success(request, "¡La casa se registró correctamente! 🏡")
            return redirect('casas:lista_casas')
        else:
            print("⚠️ Errores del formulario:", form.errors)
            messages.error(request, "Ocurrió un error al guardar la casa. Revisa la consola.")
    else:
        form = CasaForm()

    return render(request, 'inicio/crear_casa.html', {'form': form})

@login_required
@user_passes_test(es_admin)
def editar_casa(request, pk):
    casa = get_object_or_404(Casa, pk=pk)
    if request.method == 'POST':
        form = CasaForm(request.POST, request.FILES, instance=casa)
        if form.is_valid():
            form.save()
            messages.success(request, "Casa editada correctamente ✅")
            return redirect('casas:lista_casas')
    else:
        form = CasaForm(instance=casa)
    return render(request, 'inicio/editar_casa.html', {'form': form})

@login_required
@user_passes_test(es_admin)
def eliminar_casa(request, pk):
    casa = get_object_or_404(Casa, pk=pk)
    if request.method == 'POST':
        casa.delete()
        messages.success(request, "Casa eliminada correctamente 🗑️")
        return redirect('casas:lista_casas')
    return render(request, 'inicio/eliminar_casa.html', {'casa': casa})

# ==============================
# PÁGINAS GENERALES
# ==============================
def principal(request):
    return render(request, 'inicio/principal.html')

def contacto(request):
    return render(request, 'inicio/contacto.html')

def blog(request):
    return render(request, 'inicio/blog.html')

# ==============================
# PROMOCIONES — SOLO ADMIN
# ==============================
def lista_promociones(request):
    promociones = Promocion.objects.all().order_by("-fecha_creacion")
    return render(request, "inicio/promociones.html", {"promociones": promociones})

@login_required
@user_passes_test(es_admin)
def crear_promocion(request):
    if request.method == "POST":
        form = PromocionForm(request.POST)
        if form.is_valid():
            promocion = form.save(commit=False)
            promocion.creado_por = request.user
            promocion.save()
            messages.success(request, "¡Promoción creada correctamente! 🎉")
            return redirect("casas:lista_promociones")
    else:
        form = PromocionForm()
    return render(request, "inicio/crear_promociones.html", {"form": form})

@login_required
@user_passes_test(es_admin)
def eliminar_promocion(request, promocion_id):
    promocion = get_object_or_404(Promocion, id=promocion_id)
    promocion.delete()
    messages.success(request, "Promoción eliminada correctamente 🗑️")
    return redirect("casas:lista_promociones")
