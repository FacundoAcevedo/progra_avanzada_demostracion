from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    DeleteView,
    UpdateView,
    TemplateView)
from pelicula.models import (Genero, Pelicula, Cliente, Prestamo)


# INDEX
class IndexView(TemplateView):
    template_name = "pelicula/index.html"

# GENERO


class ListaGenero(ListView):
    template_name = "pelicula/listado.html"
    model = Genero

    def get_context_data(self, **kwargs):
        context = super(ListaGenero, self).get_context_data(**kwargs)
        context["titulo"] = "generos"

        return context


class CrearGenero(CreateView):
    template_name = "pelicula/formulario_creacion.html"
    model = Genero

    fields = ['codigo', 'descripcion']

    def get_context_data(self, **kwargs):
        context = super(CrearGenero, self).get_context_data(**kwargs)
        context["titulo"] = "genero"
        context["success_url"] = reverse_lazy("lista_genero")

        return context


class ModificarGenero(UpdateView):
    model = Genero
    fields = ['codigo', 'descripcion']

    def get_context_data(self, **kwargs):
        context = super(ModificarGenero, self).get_context_data(**kwargs)
        context["titulo"] = "Generos"
        context["success_url"] = reverse_lazy("lista_genero")

        return context


class EliminarGenero(DeleteView):
    template_name = "pelicula/confirmar_eliminacion.html"
    model = Genero

    def get_context_data(self, **kwargs):
        context = super(EliminarGenero, self).get_context_data(**kwargs)
        context["titulo"] = "genero"
        context["objeto_a_borrar"] = Genero.objects.get(pk=self.kwargs['pk'])
        context["success_url"] = reverse_lazy("lista_genero")

        return context


class InformeGenero(ListView):
    template_name = "pelicula/informe.html"
    model = Genero

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = "genero"

        return context

# PELICULA


class ListaPelicula(ListView):
    template_name = "pelicula/listado.html"
    model = Pelicula

    def get_context_data(self, **kwargs):
        context = super(ListaPelicula, self).get_context_data(**kwargs)
        context["titulo"] = "Peliculas"

        return context


class CrearPelicula(CreateView):
    template_name = "pelicula/formulario_creacion.html"
    model = Pelicula
    fields = ['nombre', 'estreno', 'genero']

    def get_context_data(self, **kwargs):
        context = super(CrearPelicula, self).get_context_data(**kwargs)
        context["titulo"] = "pelicula"
        context["success_url"] = reverse_lazy("listado_pelicula")

        return context


class ModificarPelicula(UpdateView):
    template_name = "pelicula/formulario_modificacion.html"
    model = Pelicula
    fields = ['nombre', 'estreno', 'genero']

    def get_context_data(self, **kwargs):
        context = super(ModificarPelicula, self).get_context_data(**kwargs)
        context["titulo"] = "pelicula"
        context["success_url"] = reverse_lazy("listado_pelicula")

        return context


class EliminarPelicula(DeleteView):
    template_name = "pelicula/confirmar_eliminacion.html"
    model = Pelicula

    def get_context_data(self, **kwargs):
        context = super(EliminarPelicula, self).get_context_data(**kwargs)
        context["titulo"] = "pelicula"
        context["objeto_a_borrar"] = Pelicula.objects.get(pk=self.kwargs['pk'])
        context["success_url"] = reverse_lazy("listado_pelicula")

        return context


class InformePelicula(ListView):
    template_name = "pelicula/informe.html"
    model = Pelicula

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = "pelicula"

        return context

# PRESTAMO


class ListaPrestamo(ListView):
    template_name = "pelicula/listado.html"
    model = Prestamo

    def get_context_data(self, **kwargs):
        context = super(ListaPrestamo, self).get_context_data(**kwargs)
        context["titulo"] = "Prestamos"

        return context


class CrearPrestamo(CreateView):
    template_name = "pelicula/formulario_creacion.html"
    model = Prestamo
    fields = ["fecha", "fecha_devolucion", "pelicula"]

    def get_context_data(self, **kwargs):
        context = super(CrearPrestamo, self).get_context_data(**kwargs)
        context["titulo"] = "prestamo"
        context["success_url"] = reverse_lazy("listado_prestamo")

        return context


class ModificarPrestamo(UpdateView):
    template_name = "pelicula/formulario_modificacion.html"
    model = Prestamo
    fields = ["fecha", "fecha_devolucion", "pelicula"]

    def get_context_data(self, **kwargs):
        context = super(ModificarPrestamo, self).get_context_data(**kwargs)
        context["titulo"] = "prestamo"
        context["success_url"] = reverse_lazy("listado_prestamo")

        return context


class EliminarPrestamo(DeleteView):
    template_name = "pelicula/confirmar_eliminacion.html"
    model = Prestamo

    def get_context_data(self, **kwargs):
        context = super(EliminarPrestamo, self).get_context_data(**kwargs)
        context["titulo"] = "prestamo"
        context["objeto_a_borrar"] = Prestamo.objects.get(pk=self.kwargs['pk'])
        context["success_url"] = reverse_lazy("listado_prestamo")

        return context

# CLIENTE


class ListaCliente(ListView):
    template_name = "pelicula/listado.html"
    model = Cliente

    def get_context_data(self, **kwargs):
        context = super(ListaCliente, self).get_context_data(**kwargs)
        context["titulo"] = "Clientes"

        return context


class CrearCliente(CreateView):
    template_name = "pelicula/formulario_creacion.html"
    model = Cliente
    fields = ["nombre", "telefono", "email"]

    def get_context_data(self, **kwargs):
        context = super(CrearCliente, self).get_context_data(**kwargs)
        context["titulo"] = "cliente"
        context["success_url"] = reverse_lazy("listado_clientes")

        return context


class ModificarCliente(UpdateView):
    template_name = "pelicula/formulario_modificacion.html"
    model = Cliente
    fields = ["nombre", "telefono", "email"]

    def get_context_data(self, **kwargs):
        context = super(ModificarCliente, self).get_context_data(**kwargs)
        context["titulo"] = "cliente"
        context["success_url"] = reverse_lazy("listado_clientes")

        return context


class EliminarCliente(DeleteView):
    template_name = "pelicula/confirmar_eliminacion.html"
    model = Cliente

    def get_context_data(self, **kwargs):
        context = super(EliminarCliente, self).get_context_data(**kwargs)
        context["titulo"] = "cliente"
        context["objeto_a_borrar"] = Cliente.objects.get(pk=self.kwargs['pk'])
        context["success_url"] = reverse_lazy("listado_clientes")

        return context
