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

### Crear base de datos para tests
Si da problemas al crear la base de datos de prueba hacer:
```
$ ALTER USER ptmadmin CREATEDB;
```

### Instalar Selenium
Para correr pruebas con [Selenium](http://selenium-python.readthedocs.io/) primero necesitas instalar el paquete:
```
$ pip install selenium
```

Se utilizará Firefox para ejecutar las pruebas, por lo que necesitas descargarle un driver [aquí](https://github.com/mozilla/geckodriver/releases/tag/v0.19.0) dependiendo de tu **SO**.

Si usas **Linux**, asegurate que el driver está en el **PATH** , colocalo en  */usr/bin* o */usr/local/bin*.

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

## Integrar Con Buildbot

### Para utilizar las herramientas de integracion continua de builbot, primero:
Para crear el servidor master:
```
$ buildbot create-master *directorio*
```
 Para ejecutar el servidor master:
```
$ buildbot start master
```
 Para crear el o los workers:
```
$ buildbot-worker create-worker *worker-model* *hostname* *worker-name* *worker-pass*
 El nombre y el worker name debe tambier ser configurado en master/master.cfg
```
 Para ejecutar el o los workers:
```
$ buildbot-worker start worker
```
###Para configurar master y workers:
 Revisar la carpeta buildbot_files y sus directorios internos.

 Crear master y workers segun sea necesario, explicado aca:
* http://docs.buildbot.net/current/tutorial/

### Configurar para cada rama:

 En master/master.cfg se tienen las secciones de *CHANGESOURCES* y
*SCHEDULERS*, cada una apuntando a un repo de git y su branch respectiva, para
cada una ajustar el repo y branch necesarios ademas de agregar los *test nuevos*
en la seccion de *BUILDERS* asi como cualquier otro worker necesario para
correrlos en la misma seccion

### Cualquier cambio a la configuracion de master.cfg debe ser seguido de:
```
$ buildbot reconfig master
$ buildbot restart master
```

### Cualquier cambio a la configuracion de algun worker:
```
$ buildbot-worker restart worker-name
```