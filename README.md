# PTmAcordeon

1. Hacer pip install para tener las apps necesarias
```
pip install -r requirements.txt
```

2. Crear base de datos en el shell de postgres
```
CREATE DATABASE db_phoenix;
```
+ Se crea el usuario
```
CREATE USER ptmadmin WITH PASSWORD 'phoenix';
```
+ Se altera el usuario
```
ALTER ROLE ptmadmin SET client_encoding TO 'utf8';
ALTER ROLE ptmadmin SET default_transaction_isolation TO 'read committed';
ALTER ROLE ptmadmin SET timezone TO 'UTC';
```

+ Por ultimo se le asignan los privilegios

```
GRANT ALL PRIVILEGES ON DATABASE db_phoenix TO ptmadmin;
ALTER USER ptmadmin CREATEDB;
```

3. Proceder a hacer las migraciones

```
python manage.py makemigrations
python manage.py migrate
```

4. Si les da error en migraciones agregar
``` null=True``` al field **name** en **main.models.AccordionAbstract**

Hacer las migraciones y quitar **null=True**
Magic!

