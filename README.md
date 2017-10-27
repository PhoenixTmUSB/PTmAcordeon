![Imgur](https://i.imgur.com/42nxmp5.png)
# TUIsD:Tool of User Interfaces Design 
Ayudante para la creación de patrones de diseño

## Patrones actuales

* [Acordeón](http://www.welie.com/patterns/showPattern.php?patternID=minesweeping)
* [Minesweeper](http://www.welie.com/patterns/showPattern.php?patternID=accordion)
## Intalación y ejecución

### Clonar el repositorio
```
$ git clone https://github.com/PhoenixTmUSB/PTmAcordeon.git
```
### Preparación del entorno
1. Moverse a la carpeta donde está el proyecto django
```
$ cd PTmAcordeon/phoenix
```
2. Hacer pip install para tener las apps necesarias
```
$ pip install -r requirements.txt
```

2. Crear base de datos en el shell de postgres
```
=# CREATE DATABASE db_phoenix;
```
+ Se crea el usuario
```
=# CREATE USER ptmadmin WITH PASSWORD 'phoenix';
```
+ Se altera el usuario
```
=# ALTER ROLE ptmadmin SET client_encoding TO 'utf8';
=# ALTER ROLE ptmadmin SET default_transaction_isolation TO 'read committed';
=# ALTER ROLE ptmadmin SET timezone TO 'UTC';
```

+ Por ultimo se le asignan los privilegios

```
=# GRANT ALL PRIVILEGES ON DATABASE db_phoenix TO ptmadmin;
=# ALTER USER ptmadmin CREATEDB;
```
3. Proceder a hacer las migraciones
```
$ python manage.py makemigrations
$ python manage.py migrate
```

### Ejecución 

Para ejecutarlo utilizando el servidor que trae consigo **Django**, ejecutar:
```
$ python manage.py runserver
```

## Pruebas

Se realizaron pruebas unitarias y pruebas de integración, algunas con [Selenium](http://selenium-python.readthedocs.io/).

### Instalar Selenium
Para correr pruebas con [Selenium](http://selenium-python.readthedocs.io/) primero necesitas instalar el paquete:
```
$ pip install selenium
```

Se utilizará Firefox para ejecutar las pruebas, por lo que necesitas descargarle un driver [aquí](https://github.com/mozilla/geckodriver/releases/tag/v0.19.0) dependiendo de tu **SO**.

Si usas **Linux**, asegurate que el driver está en el **PATH** , colocalo en  */usr/bin* or */usr/local/bin*.

### Ejecutar las pruebas

Para correr **todas las pruebas**, ejecuta:
```
$ python manage.py test minesweep/tests/
$ python manage.py test accordion/tests/
```

Para ejecutar las pruebas con **Selenium** solamente:
```
$ python manage.py test minesweep/tests/tests_selenium/
$ python manage.py test accordion/tests/tests_selenium/
```
Para ejecutar las pruebas que no utilizan **Selenium**:
```
$ python manage.py test minesweep/tests/tests_normales/
$ python manage.py test accordion/tests/tests_normales/
```

## Enlaces de ayuda
* https://docs.djangoproject.com/en/1.11/


