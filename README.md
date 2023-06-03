# Open Lyrics Search <!-- omit in toc -->

- [Guía De Instalación](#guía-de-instalación)
    - [Pre Requisitos](#pre-requisitos)
    - [Loader](#loader)
    - [API](#api)
    - [React App](#react-app)
- [Guía De Uso](#guía-de-uso)
    - [Loader](#loader-1)
    - [API](#api-1)
        - [Full Text Search](#full-text-search)
        - [Consulta De Canciones Por ID](#consulta-de-canciones-por-id)
    - [React App](#react-app-1)
- [Pruebas Realizadas](#pruebas-realizadas)
    - [Loader](#loader-2)
    - [API](#api-2)
- [Resultados Pruebas Unitarias](#resultados-pruebas-unitarias)
    - [Loader](#loader-3)
        - [TestDataLoader](#testdataloader)
    - [API](#api-3)
        - [TestPipelines](#testpipelines)
- [Recomendaciones](#recomendaciones)
- [Conclusiones](#conclusiones)

## Guía De Instalación

### Pre Requisitos

* Clonar el repositorio a la máquina local.
* [Docker Desktop](https://www.docker.com/products/docker-desktop/).
* Alguna herramienta para enviar peticiones HTTP como [Postman](https://www.postman.com/downloads/).

### Loader

No es necesario instalar nada, ya que se utiliza una imagen que está disponible en Docker Hub.

### API

No es necesario instalar nada de este módulo, ya que el API se encuentra corriendo en Azure Container Apps.

### React App

No es necesario instalar nada de este módulo, ya que la aplicación se encuentra corriendo en Azure App Service.

## Guía De Uso

### Loader

1. Abrir Docker Desktop.
2. Abrir una terminal en la máquina local.
3. Ir al directorio **src/loader**.
4. Ejecutar el comando `docker compose up` o `docker compose up -d` si no se desea ver los logs de los contenedores en la terminal.

### API

#### Full Text Search

1. Abrir la herramienta para enviar peticiones HTTP.
2. Utilizar el endpoint https://main-app.mangoocean-f33b36da.eastus.azurecontainerapps.io/open-lyrics-search/songs con método GET.
3. Se recibiran los siguientes parámetros en la petición:
    * search
        * Obligatorio.
        * Representa la búsqueda de texto que se hará sobre las canciones.
        * Si se pone el término entre **""**, se hará una búsqueda de frase exacta.
    * genre
        * Opcional.
        * Representa el género músical por el cual se quieren filtrar las canciones.
        * Puede haber más de uno.
    * artist
        * Opcional.
        * Representa el nombre del artista por el cual se quieren filtrar las canciones.
        * Puede haber más de uno.
    * popularity
        * Opcional.
        * Representa la popularidad del artista por la cual se quieren filtrar las canciones.
        * Puede ser uno (se toma como un límite inferior) o dos (se toma como un rango) de estos parámetros.
    * songs
        * Opcional.
        * Representa la cantidad de canciones del artista por la cual se quieren filtrar las canciones.
        * Puede ser uno (se toma como un límite inferior) o dos (se toma como un rango) de estos parámetros.
4. Para poner parámetros en el request, se debe poner un **?** al final del endpoint y escribir los parámetros de la siguiente forma:
    * parameter=value&parameter=value...
    * El endpoint quedaría: https://main-app.mangoocean-f33b36da.eastus.azurecontainerapps.io/open-lyrics-search/songs?parameter=value&parameter=value
5. Al ejecutar la petición se recibirá un documentos con 2 keys:
    * Facets
        * Contiene los facets que se generaron de las canciones con la búsqueda realizada.
            * Los facets de nombres de artista, géneros musicales y lenguaje están limitados a traer los primeros 25 agrupamientos (ordenados de mayor a menor).
    * Songs
        * Contiene el id, highlights (donde se encontraron match de la búsqueda con la canción), puntuación de la búsqueda y el nombre de la canción.

#### Consulta De Canciones Por ID

1. Abrir la herramienta para enviar peticiones HTTP.
2. Utilizar el endpoint https://main-app.mangoocean-f33b36da.eastus.azurecontainerapps.io/open-lyrics-search/songs/id con método GET.
3. Sustituir id por el id de la canción que se desea buscar.
4. Ejecutar la petición.
5. Se retornará un documento con toda la información de la canción.

### React App

1. Entrar al siguiente [link](http://main-alpha.azurewebsites.net/).
2. Si no se posee una cuenta en la página presionar el botón de registrarse, de lo contrario llenar los campos de correo y contraseña solicitados y presionar el botón de iniciar sesión y pasar al paso 4.
3. Si se presionó el botón de registrarse llenar los campos con la información solicitada y presionar el botón de registrarse.
4. Seguidamente aparece una pantalla donde el usuario tiene que llenar el espacio con algún detalle de una canción de su interés y presionar el botón de buscar, si se desea cerrar sesión en algún momento solamente es necesario presionar el botón de cerrar sesión ubicado en la esquina superior derecha y será devuelto a la página de iniciar sesión.
5. Una vez presionado el botón de buscar será enviado a la página principal de búsquedas donde después de esperar unos segundos aparecerán los primeros 100 resultados obtenidos, así como una parte donde podrá buscar una nueva canción, así como filtrar los resultados obtenidos. Para poder utilizar los filtros simplemente es necesario presionar el botón de filtros, luego elegir que filtros quiere usar presionando sobre ellos.
6. Para ver más detalles acerca de una canción es necesario presionar sobre el nombre de alguna de estas, luego de esto será enviado a una página con todos los detalles acerca de la canción seleccionada. Para volver a buscar canciones solamente se necesita presionar el botón volver y será enviado devuelta a la página principal de búsquedas.

## Pruebas Realizadas

### Loader

El loader fue probado con 4 archivos, los 2 archivos fuente y 2 archivos creados por el equipo. Esto se hizo con la intención de comprobar que el loader funcionara con más archivos de los suministrados.

### API

Se realizaron distintas peticiones HTTP con Postman probando distintas combinaciones de parámetros, algunas fueron:

* https://main-app.mangoocean-f33b36da.eastus.azurecontainerapps.io/open-lyrics-search/songs?search=center core never more
* https://main-app.mangoocean-f33b36da.eastus.azurecontainerapps.io/open-lyrics-search/songs?search="I got a laptop in my back pocket"
* https://main-app.mangoocean-f33b36da.eastus.azurecontainerapps.io/open-lyrics-search/songs?search=I got a laptop in my back pocket
* https://main-app.mangoocean-f33b36da.eastus.azurecontainerapps.io/open-lyrics-search/songs?search=house&genre=rap
* https://main-app.mangoocean-f33b36da.eastus.azurecontainerapps.io/open-lyrics-search/songs?search=today&artist=Slipknot&genre=rock

## Resultados Pruebas Unitarias

### Loader

#### TestDataLoader

Todas las pruebas aprobaron. Estas pruebas fueron de gran utilidad ya que ayudó a saber rápidamente si los csv se estaban procesando correctamente y si la información se conectaba como debia.

### API

#### TestPipelines



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
