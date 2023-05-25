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

1. Abrir una terminal.
2. Ir al directorio **src/loader**.
3. Ejecutar el comando `.\build.bat`.

### API

### React App

## Guía De Uso

### Loader

1. Abrir una terminal.
2. Ir al directorio **src/loader**.
3. Ejecutar el comando `docker compose up` o `docker compose up -d` si no se desea ver los logs de los contenedores en la terminal.

### API

### React App

## Pruebas Realizadas

### Loader

El loader fue probado con 4 archivos, los 2 archivos fuente y 2 archivos creados por el equipo. Esto se hizo con la intención de comprobar que el loader funcionara con más archivos de los suministrados.

### API

### React APP

## Resultados Pruebas Unitarias

### Loader

### API

## Recomendaciones

## Conclusiones