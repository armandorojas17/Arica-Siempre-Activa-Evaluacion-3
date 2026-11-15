from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import ActividadForm
from .models import Actividad


@login_required
def ActividadCreateView(request):

    if not hasattr(request.user, 'perfil') or request.user.perfil.rol != 'gremio':
        return redirect('/')

    form = ActividadForm(
        request.POST or None,
        request.FILES or None
    )

    if request.method == "POST":
        if form.is_valid():
            actividad = form.save(commit=False)
            actividad.organizador = request.user
            actividad.save()

            messages.success(
                request,
                "Actividad creada correctamente."
            )
            return redirect('listar_gremio')

    return render(
        request,
        'panel_gremio/actividad_gremio_form.html',
        {'accion': 'Crear', 'form': form}
    )


@login_required
def ActividadListView(request):

    if not hasattr(request.user, 'perfil') or request.user.perfil.rol != 'gremio':
        return redirect('/')

    actividades = Actividad.objects.filter(
        organizador=request.user
    )

    return render(
        request,
        'panel_gremio/actividad_gremio_list.html',
        {'actividades': actividades}
    )


@login_required
def ActividadUpdateView(request, id):

    if not hasattr(request.user, 'perfil') or request.user.perfil.rol != 'gremio':
        return redirect('/')

    actividad = get_object_or_404(
        Actividad,
        pk=id,
        organizador=request.user
    )

    form = ActividadForm(
        request.POST or None,
        request.FILES or None,
        instance=actividad
    )

    if request.method == "POST":
        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Actividad actualizada correctamente."
            )
            return redirect('listar_gremio')

    return render(
        request,
        'panel_gremio/actividad_gremio_form.html',
        {'accion': 'Actualizar', 'form': form}
    )


@login_required
def ActividadDeleteView(request, id):

    if not hasattr(request.user, 'perfil') or request.user.perfil.rol != 'gremio':
        return redirect('/')

    actividad = get_object_or_404(
        Actividad,
        pk=id,
        organizador=request.user
    )

    if request.method == "POST":
        actividad.delete()

        messages.success(
            request,
            "Actividad eliminada correctamente."
        )

        return redirect('listar_gremio')

    return redirect('listar_gremio')