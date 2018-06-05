from django.contrib import admin

from pelicula.models import Cliente, Genero, Pelicula, Prestamo

admin.site.register(Cliente)
admin.site.register(Genero)
admin.site.register(Pelicula)
admin.site.register(Prestamo)
