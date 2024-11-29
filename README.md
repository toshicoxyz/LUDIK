# Instrucciones para Levantar el Proyecto con Docker
# Primera parte de prueba

## Explicacion de primera etapa

Me amaneci haciendo la prueba ya que tengo un trabajo temporal que me veo obligado hacer de noche :(, aun asi termine la primera etapa segun el tiempo elegi python para el backend ya q hace poco toque el lenguaje en odoo, decidi dockerizar el proyecto para que no tengas problemas de dependencias ya que se aisla el proyecto y tmb si me da tiempo la base de datos para que de un solo click puedas usar.

## Requisitos Previos

Antes de comenzar, asegúrate de tener instalados los siguientes programas en tu máquina:

1. **Docker**: Docker es una herramienta que te permite crear, implementar y ejecutar aplicaciones dentro de contenedores. Si no tienes Docker instalado, puedes descargarlo desde [aquí](https://www.docker.com/get-started).

2. **Docker Compose**: Docker Compose es una herramienta para definir y ejecutar aplicaciones Docker con múltiples contenedores. Docker Compose generalmente se instala junto con Docker, pero si no lo tienes, puedes seguir las instrucciones de instalación [aquí](https://docs.docker.com/compose/install/).

## Pasos para Levantar el Proyecto con Docker

Sigue estos pasos para levantar el proyecto en tu máquina utilizando Docker.

### 1. Clonar el Repositorio

Primero, clona el repositorio del proyecto en tu máquina local. Abre una terminal y usa el siguiente comando:

```bash
git clone https://github.com/toshicoxyz/LUDIK
```

Este comando descargará todos los archivos del proyecto en una carpeta llamada `LUDIK`.

### 2. Navegar a la Carpeta del Proyecto

En la terminal, navega a la carpeta del proyecto que acabas de clonar:

```bash
cd LUDIK
```

### 3. Revisar el Dockerfile

Asegúrate de que el archivo `Dockerfile` esté presente en el directorio raíz de tu proyecto. Este archivo es el que Docker usará para construir la imagen del contenedor.

### 4. Revisar el Archivo `docker-compose.yml`

El archivo `docker-compose.yml` es responsable de definir cómo se deben ejecutar los contenedores. Verifica que esté presente en el proyecto. Este archivo contiene configuraciones para la base de datos, servidor backend, frontend, entre otros, dependiendo de la arquitectura de tu proyecto.

### 5. Construir y Levantar los Contenedores con Docker Compose

En la terminal, ejecuta el siguiente comando para construir y levantar los contenedores:

```bash
docker-compose up --build
```

Este comando hará lo siguiente:

- **`--build`**: Construye las imágenes de los contenedores según lo definido en el `Dockerfile` y `docker-compose.yml`.
- Levanta todos los contenedores necesarios para el proyecto (por ejemplo, base de datos, servidor de backend, frontend, etc.).

El primer arranque puede tardar algunos minutos ya que Docker necesita descargar las imágenes base y construir las imágenes personalizadas.

### 6. Verificar que los Contenedores Están Corriendo

Una vez que se haya ejecutado el comando `docker-compose up --build`, deberías ver algo similar a lo siguiente en tu terminal:

```
Starting backend ... done
Starting frontend  ... done
```

Esto indica que los contenedores se han iniciado correctamente.

### 7. Acceder a la Aplicación

Si todo se ha ejecutado correctamente, ahora puedes acceder a tu aplicación en un navegador web.

- **Backend**: Si el backend está configurado para correr en el puerto `8080`, abre tu navegador y accede a:  
  `http://localhost:8000`

- **Frontend**: Si el frontend está configurado para correr en el puerto `3000`, abre tu navegador y accede a:  
  `http://localhost:3000`

(Estos puertos pueden variar dependiendo de la configuración de tu proyecto, así que revisa el archivo `docker-compose.yml` si no estás seguro).

### 8. Detener los Contenedores

Si deseas detener los contenedores, simplemente ejecuta el siguiente comando en la terminal dentro de la carpeta del proyecto:

```bash
docker-compose down
```

Este comando detendrá y eliminará los contenedores, pero no eliminará las imágenes construidas.

### 9. Solución de Problemas

Si encuentras algún problema, aquí hay algunas soluciones comunes:

- **Problema**: "Puerto en uso".
  - Si ves un error como "puerto en uso", significa que otro servicio ya está utilizando el puerto que Docker está intentando usar. Puedes cambiar el puerto en el archivo `docker-compose.yml` o detener el servicio que está utilizando ese puerto.

- **Problema**: "No se puede conectar a la base de datos".
  - Asegúrate de que la base de datos esté corriendo correctamente en su contenedor. Verifica los logs con `docker-compose logs` y revisa si hay algún error.

- **Problema**: "El contenedor no se construye correctamente".
  - Revisa el archivo `Dockerfile` y `docker-compose.yml` para asegurarte de que las configuraciones son correctas y las dependencias están bien definidas.

---

## Comandos Útiles

- **Ver los contenedores en ejecución**:

```bash
docker ps
```

- **Ver los logs de un contenedor**:

```bash
docker-compose logs
```

- **Eliminar los contenedores, imágenes y volúmenes**:

```bash
docker-compose down --volumes --rmi all
```

Este comando eliminará tanto los contenedores como las imágenes y los volúmenes asociados.

---



