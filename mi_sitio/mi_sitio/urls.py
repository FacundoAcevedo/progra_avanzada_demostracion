"""mi_sitio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from pelicula.views import (
    ListaGenero,
    CrearGenero,
    ModificarGenero,
    EliminarGenero,
    InformeGenero)
from pelicula.views import (
    ListaPelicula,
    CrearPelicula,
    ModificarPelicula,
    EliminarPelicula,
    InformePelicula)
from pelicula.views import (
    ListaPrestamo,
    CrearPrestamo,
    ModificarPrestamo,
    EliminarPrestamo)
from pelicula.views import (
    ListaCliente,
    CrearCliente,
    ModificarCliente,
    EliminarCliente)
from pelicula.views import IndexView

urlpatterns = [

    url('admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name="Index"),

    url(r'^genero/$', ListaGenero.as_view(), name="lista_genero"),
    url(r'^genero/crear/$', CrearGenero.as_view(success_url="/genero/"), name="crear_genero"),
    url(r'^genero/modificar/(?P<pk>\d+)$', ModificarGenero.as_view(success_url="/genero/"), name="modificar_genero"),
    url(r'^genero/eliminar/(?P<pk>\d+)$', EliminarGenero.as_view(success_url="/genero/"), name="eliminar_genero"),
    url(r'^genero/informe/$', InformeGenero.as_view(), name="informe_genero"),

    url(r'^pelicula/$', ListaPelicula.as_view(), name="listado_pelicula"),
    url(r'^pelicula/crear/$', CrearPelicula.as_view(success_url="/pelicula/"), name="crear_pelicula"),
    url(r'^pelicula/modificar/(?P<pk>\d+)$', ModificarPelicula.as_view(success_url="/pelicula/"), name="modificar_pelicula"),
    url(r'^pelicula/eliminar/(?P<pk>\d+)$', EliminarPelicula.as_view(success_url="/pelicula/"), name="eliminar_pelicula"),
    url(r'^pelicula/informe/$', InformePelicula.as_view(), name="informe_pelicula"),

    url(r'^prestamo/$', ListaPrestamo.as_view(), name="listado_prestamo"),
    url(r'^prestamo/crear/$', CrearPrestamo.as_view(success_url="/prestamo/"), name="crear_prestamo"),
    url(r'^prestamo/modificar/(?P<pk>\d+)$', ModificarPrestamo.as_view(success_url="/prestamo/"), name="modificar_prestamo"),
    url(r'^prestamo/eliminar/(?P<pk>\d+)$', EliminarPrestamo.as_view(success_url="/prestamo/"), name="eliminar_prestamo"),

    url(r'^cliente/$', ListaCliente.as_view(), name="listado_clientes"),
    url(r'^cliente/crear/$', CrearCliente.as_view(success_url="/cliente/"), name="crear_cliente"),
    url(r'^cliente/modificar/(?P<pk>\d+)$', ModificarCliente.as_view(success_url="/cliente/"), name="modificar_cliente"),
    url(r'^cliente/eliminar/(?P<pk>\d+)$', EliminarCliente.as_view(success_url="/cliente/"), name="eliminar_cliente"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
