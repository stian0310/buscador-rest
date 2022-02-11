# Buscador REST

API Para gestionar busquedas con motor de wikipedia, guardando las solicitudes mas requeridas

## <div id= "Started"></div> Getting Started

Para ejecutar la prueba se necesita configurar las variables de entorno en un archivo .env

Las variables necesarias se encuentran en el archivo de ejemplo .env.example

Para ejecutar el codigo se necesita correr el proyecto desde docker.
Lo primero es crear la imagen donde correra el entorno de django:

```sh
$ docker-compose build
```

Una vez se contruye la imagen para el entorno de django levantamos los servicios:

```
$ docker-compose up
```

La primera vez que lanzamos los servicios no funcionaran pues hacen falta configuraciones dentro de los entornos.

La imagen de postgress debera descargarse y el servicio se configurara con las variables de usuario del docker-compose.
La imagen de django intentara establecer conexion con la base de datos, en la primera ejecucion lo normal es que falle, al no estar disponible aun el servicio.

Cuando el comando docker-compose up no ejecute mas acciones y los servicios queden en espera, podemos correr las migraciones del proyecto.

Para esto desde otra terminal ejecutamos:
```
$ docker-compose ps
```
Podemos ubicar el contenedor del proyecto por el nombre de la imagen: buscador-rest_app y su respectivo CONTAINER ID.

A continuacion vamos a entrar en el contenedor del servicio de django para correr las migraciones:

```
$ docker exec -it CONTAINER ID bash
```
remplazamos CONTAINER ID por el numero de nuestro contendor, ejemplo CONTAINER ID: 22fe87b07900

```
$ docker exec -it 22fe87b07900 bash
```

esto lanzara una consola interactiva dentro del contenedor de django.

Ahora podemos ejecutar las migraciones (python manage.py migrate):

```
root@22fe87b07900:/code# python manage.py migrate
```

Una vez terminado, procedemos con la creacion del superuser del sistema (python manage.py createsuperuser):

```
root@22fe87b07900:/code# python manage.py createsuperuser
```

se nos pedira la informacion para el usuario:
- email
- username
- first name
- last name
- password
- password (again)

y con esto terminaremos el proceso:

```
root@22fe87b07900:/code# exit
```

Volvemos a la consola donde tenemos docker-compose corriendo y lo detenemos tambien con ctrl+c

Ahora podemos correr denuevo docker-compose up y todo deberia funcionar sin problema

```
$ docker-compose up
```

si queremos correr en segundo plano:
```
$ docker-compose up -d
```

Desde el navegador web podremos acceder a http://localhost:8000/APIv1/redoc/ o http://localhost:8000/APIv1/swagger/
para ver la informacion de como podemos consumir la API del proyecto

Tambien para tenemos acceso al admin de django para revisar los datos que se agreguen a la base de datos.
