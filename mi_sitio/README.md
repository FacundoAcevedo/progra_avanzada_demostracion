# ABM de Videclub


Cree un fixture con datos para chequear la app, estas son las instrucciones
para correrla con los datos:

```
pip install -r requirement.txt

./manage.py migrate --run-syncdb

# Cargamos el fixture
./manage.py loaddata pelicula/fixtures/initial_data.json
./manage.py  runserver
```


Alumno: Facundo M. Acevedo
Legajo: 95572
Año: 2017
Licencia: gplv3+
