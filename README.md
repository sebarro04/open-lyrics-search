# Open Lyrics Search <!-- omit in toc -->

- [Guía De Instalación](#guía-de-instalación)
  - [Pre Requisitos](#pre-requisitos)
  - [Infraestructura Azure](#infraestructura-azure)
  - [Loader](#loader)
  - [API](#api)
  - [React App](#react-app)
- [Guía De Uso](#guía-de-uso)
  - [Loader](#loader-1)
  - [API](#api-1)
  - [React App](#react-app-1)
- [Pruebas Realizadas](#pruebas-realizadas)
  - [Loader](#loader-2)
  - [API](#api-2)
  - [React APP](#react-app-2)
- [Resultados Pruebas Unitarias](#resultados-pruebas-unitarias)
  - [Loader](#loader-3)
  - [API](#api-3)
- [Recomendaciones](#recomendaciones)
- [Conclusiones](#conclusiones)

## Guía De Instalación

### Pre Requisitos

* [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli)
* [Docker Desktop](https://www.docker.com/products/docker-desktop/)

### Infraestructura Azure

1. Abrir una terminal.
2. Ejecutar el comando `az login --use-device-code` para iniciar sesión con Azure CLI.
3. Abrir el archivo **src/infrastructure/conf/group.tfvars**.
4. Establecer un nombre para el grupo sin caracteres especiales, espacios o mayusculas.
5. Abrir el archivo **src/infrastructure/container_services.tf**.
6. En el key **app_settings** se deben agregar las variables de entorno que vaya a necesitar el app service de la siguiente forma:

```terraform
"ENV_EXAMPLE" = "VALUE"
```

7. Abrir el archivo **src/infrastructure/container_app.tf**.
8. En el key **template.container** se deben agregar las variables de entorno que vaya a necesitar el container app de la siguiente forma (c/u):

```terraform
env {
    name = "ENV_EXAMPLE"
    value = "VALUE"
}
```

9. Ir al directorio **src/infrastructure**.
10. Ejecutar el comando `.\build.bat`.
    * Si se desea eliminar la infraestructura se debe ejecutar el comando `.\destroy.bat`.

### Loader

1. Abrir el archivo **src/loader/app/.env**.
2. Agregar las variables de entorno necesarias para que la aplicación funcione.
3. Abrir una terminal.
4. Ir al directorio **src/loader**.
5. Ejecutar el comando `.\build.bat`.

### API

### React App

## Guía De Uso

### Loader

1. Iniciar sesión en [Azure](https://azure.microsoft.com/es-es/get-started/azure-portal).
2. Entrar al storage account creado con la infraestructura.
3. Entrar en el apartado **containers**.
4. Entrar a **documents**.
5. Subir manualmente los archivos que serán procesados por el loader.
    * Los archivos de artistas deben ser un **.csv** y deben tener como header **Artist,Genres,Songs,Popularity,Link**
    * Los archivos de letras deben ser un **.csv** y deben tener como header **ALink,SName,SLink,Lyric,language**
        * La entrada de Lyric de cada canción debe ir entre doble comilla ("").
6. Abrir una terminal.
7. Ir al directorio **src/loader**.
8. Ejecutar el comando `docker compose up` o `docker compose up -d` si no se desea ver los logs de los contenedores en la terminal.

### API

### React App

1. Entrar al siguiente link(http://main-alpha.azurewebsites.net/).
2. Si no se posee una cuenta en la página presionar el botón de registrarse, de lo contrario llenar los campos de correo y contraseña solicitados y presionar el botón de iniciar sesión y pasar al paso 4.
3. Si se presionó el botón de registrarse llenar los campos con la información solicitada y presionar el botón de registrarse.
4. Seguidamente aparece una pantalla donde el usuario tiene que llenar el espacio con algún detalle de una canción de su interés y presionar el botón de buscar, si se desea cerrar sesión en algún momento solamente es necesario presionar el botón de cerrar sesión ubicado en la esquina superior derecha y será devuelto a la página de iniciar sesión.
5. Una vez presionado el botón de buscar será enviado a la página principal de búsquedas donde después de esperar unos segundos aparecerán los primeros 100 resultados obtenidos, así como una parte donde podrá buscar una nueva canción, así como filtrar los resultados obtenidos. Para poder utilizar los filtros simplemente es necesario presionar el botón de filtros, luego elegir que filtros quiere usar presionando sobre ellos.
6. Para ver más detalles acerca de una canción es necesario presionar sobre el nombre de alguna de estas, luego de esto será enviado a una página con todos los detalles acerca de la canción seleccionada. Para volver a buscar canciones solamente se necesita presionar el botón volver y será enviado devuelta a la página principal de búsquedas.

## Pruebas Realizadas

### Loader

El loader fue probado con 4 archivos, los 2 archivos fuente y 2 archivos creados por el equipo. Esto se hizo con la intención de comprobar que el loader funcionara con más archivos de los suministrados.

### API

### React APP

## Resultados Pruebas Unitarias

### Loader

### API

## Recomendaciones

- Se recomienda dar mantenimiento continuo para asegurarse de eliminar cualquier tipo de error a tiempo y de esta manera no crear inconvenientes a los usuarios
- Se recomienda hacer pruebas de usabilidad para tomar en cuenta los comentarios y puntos de vista de usuarios para de esta manera mejorar la interfaz de usuario.
- Compartir por algún medio de comunicación institucional la guía de uso, ya que esto facilitará a los usuario su uso.
- Poner a disposición del usuario un medio de soporte al cual puedan comunicarse en caso de cualquier tipo de inconveniente con el sistema.
- Se debe asegurar que la base se mantenga actualizada con los datos más recientes y concisos que permitan al usuario obtener información verídica y fiable.
- Se sugiere el acompañamiento de un asistente en caso de que el usuario que vaya a hacer uso de la interfaz tenga alguna dificultad de visual, ya que la actual versión no cuenta con asistente de voz.
- Se recomienda realizar pruebas periódicas de seguridad, como análisis de vulnerabilidades y pruebas de penetración, para identificar posibles brechas y mejorar la protección del sistema.
- Se recomienda acceder al sistema haciendo uso de un navegador web confiable como Google Chrome o Microsoft Edge.
- Se recomienda contar con una conexión a internet estable, para evitar la inconsistencia de los datos o los retrasos en las respuestas.
- Se aconseja leer el manual de usuario antes de hacer uso del software para obtener los mejores resultados del mismo.

## Conclusiones

- El uso de los índices para realizar búsquedas en Mongo Atlas Search mejora el rendimiento de las consultas, por lo tanto, vuelve la implementación más eficiente. 
- El uso del componente Loader en Python facilitó descargar de archivos CSV desde Azure Blob y la cargar de la información en una o más colecciones de Mongo Atlas. 
- La utilización de Azure Blob como almacenamiento de archivos CSV ofreció una solución escalable y confiable para almacenar y acceder a los archivos requeridos para el proyecto.
- Al usar Loader se pudo automatizar los procesos solicitados, asegurando la integridad y consistencia de la información en el sistema.
- Los tutoriales proporcionados por Mongo Atlas para crear y configurar índices agilizaron la implementación de los mismos, permitiendo obtener los resultados deseados de una manera más rápida sin tener que invertir demasiado tiempo en la búsqueda de estos.
- El uso de pruebas unitarias para todos los endpoints del API garantiza la calidad del código minimizando la presencia de errores en este.
- Al utilizar Firebase como una base de datos en tiempo real para el registro e inicio de sesión en la aplicación React, esto proporcionó una forma segura y confiable de gestionar la autenticación de los usuarios.
- El uso de React como framework para desarrollar la aplicación web proporcionó una estructura modular y escalable para la interfaz de usuario.
- Se logró implementar de manera correcta la página de búsqueda que permite al usuario realizar búsquedas estilo Google en las letras de canciones. Y también se proporcionan opciones de filtrado (facets) por artista, lenguaje, género musical del artista, popularidad del artista y número de canciones del artista.
- Las herramientas utilizadas en el proyecto ofrecieron soluciones efectivas y escalables para implementar un sistema de búsqueda Full-text Search sobre letras de canciones. Estas herramientas permitieron la gestión eficiente de los datos, la interacción con la base de datos y la creación de una interfaz de usuario intuitiva y funcional.