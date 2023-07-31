# Microservicio Courses
Este microservicio se encarga del manejo de los datos y las operaciones funcionales relacionadas al dominio "Course" de la aplicación Teammates.

# Setup
Para correrlo en la máquina local, se recomienda crear un ambiente virtual en el directorio base del proyecto. En Windows el comando para la creación del ambiente virtual sería: ```python -m venv venv```
Despues se debe ingresar a la carpete "/courses" para instalar todas las librerías necesarios a través del comando ```pip install -r requirements.txt```.
Una vez terminado la instalación se puede correr el microservicio dentro de la carpeta "/courses/src" con el comando ```flask run```.

# Funcionalidades
El microservicio ofrece una API Rest con la cual se pueden realizar todas la operaciones CRUD: Crear un curso, obtener información sobre un curso o un conjunto de cursos, modificar la información de un curso, eliminar un curso y otras.
A través del siguiente enlace encuentra la documentación detallada de las posibles peticiones HTTP:
https://documenter.getpostman.com/view/20308430/2s946pYozf

# Probar el microservicio
En la carpeta del proyecto encuentra el archivo "ModernizacionCoursesService.postman_collection" el cual se puede descargar para probar el servicio en la máquina local con Postman.
Durante los días siguientes (día de hoy: 30.07.2023) se van a dejar activadas las instancias del servicio y de la base de datos que se crearon con el fin de realizar el experimento de la modernización. Por eso la dirección HTTP configurada en la colección Postman es por defecto la de la instancia del servicio en ComputeEngine de GCP:
http://34.171.169.145:5000
Si prefiere enviar las peticiones HTTP a una instancia desplegada en su máquina local, debe reemplazar la dirección HTTP por la que se configuró, por ejemplo "localhost:5000".

# Integrantes Grupo 1:
*ZARAY VIVIANA REY VIVIESCAS*
*CHRISTIAN BORRÁS TORRES*
*DAVID MORALES AGUILAR*
*PATRICK MYKODA*
