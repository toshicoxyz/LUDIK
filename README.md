# Instrucciones para Levantar el Proyecto con Docker
# Primera parte de prueba

## Explicacion de primera etapa

Me amaneci haciendo la prueba ya que tengo un trabajo temporal que me veo obligado hacer de noche :(, aun asi termine la primera etapa segun el tiempo elegi python para el backend ya q hace poco toque el lenguaje en odoo, decidi dockerizar el proyecto para que no tengas problemas de dependencias ya que se aisla el proyecto y tmb si me da tiempo la base de datos para que de un solo click puedas usar.

# No se olviden de renombrar el .env.example -> .env para que se tome las credenciales :)
# LA BASE DE DATOS CREADO POR CONTENEDOR TIENE ALGUNOS BUGS ;v no funciona por ahora

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
  `http://localhost:8020`
  La documentación de las rutas
  `http://localhost:8020/docs`

- **Frontend**: Si el frontend está configurado para correr en el puerto `3000`, abre tu navegador y accede a:  
  `http://localhost:3020`

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

## ⚠️ **ALERTA**: Problemas al levantar el contenedor del Frontend

Si el contenedor del **frontend** no se levanta correctamente y encuentras algún error relacionado con dependencias o bugs no previstos, puedes intentar las siguientes soluciones **manualmente**:

1. **Instalar las dependencias manualmente**:

   Si encuentras problemas al levantar el contenedor del frontend, navega al directorio de frontend y ejecuta los siguientes comandos para forzar la instalación de dependencias:

   ```bash
   cd LUDIK
   npm install --force
   ```

   El uso de `--force` puede resolver posibles conflictos de dependencias.

2. **Ejecutar el servidor de desarrollo manualmente**:

   Si aún después de instalar las dependencias manualmente no puedes levantar el frontend, intenta ejecutar el servidor de desarrollo directamente:

   ```bash
   npm run dev
   ```

   Esto debería iniciar el servidor en el puerto predeterminado (por ejemplo, `localhost:3000`), dependiendo de la configuración de tu proyecto.

---

## 🚧 **Problemas no previstos y solución temporal**

El proyecto puede contener bugs o configuraciones no completamente probadas. Si encuentras algún problema al ejecutar el contenedor o al interactuar con el proyecto, por favor sigue estos pasos para solucionar los problemas más comunes:

- Asegúrate de tener una versión compatible de **Node.js** y **npm**.
- Si usas un entorno de desarrollo en tu máquina local, asegúrate de que todas las dependencias están correctamente instaladas.
- Si el proyecto sigue fallando, revisa los logs y mensajes de error que aparecen en la terminal y verifica si algún servicio de Docker no se ha levantado correctamente.

¡No dudes en consultar la documentación oficial o crear un issue en el repositorio si encuentras un bug que no has podido resolver! 🚀

# Proyecto LUDIK - Optimización y Mejoras 🚀

Este proyecto ha sido optimizado con varias mejoras en cuanto a rendimiento, usabilidad y eficiencia. A continuación, se detallan las optimizaciones y ajustes implementados:

## 💻 **Optimización del Frontend**

### 🚀 **Lazy Loading de Componentes**

Para mejorar el rendimiento de carga del proyecto y reducir el tiempo de renderizado inicial, se ha implementado **Lazy Loading** de los componentes del frontend. Esto significa que los componentes se cargarán solo cuando sean necesarios, en lugar de cargarlos todos al inicio.

- Se utiliza la función `defineAsyncComponent` de Vue.js para cargar los componentes de forma asincrónica.
- Esto reduce el tamaño inicial del paquete JavaScript, mejorando los tiempos de carga y la experiencia de usuario en dispositivos con conexiones más lentas.

Ejemplo de la implementación de Lazy Loading en Vue.js:

```javascript
const FormComponent = defineAsyncComponent(() => import('@/components/TaskForm.vue'));
const ListComponent = defineAsyncComponent(() => import('@/components/TaskList.vue'));
```

### 🖼️ **Optimización de Imágenes**

Aunque el proyecto no tiene imágenes pesadas actualmente, para futuras implementaciones y para garantizar que las imágenes sean lo más eficientes posible, hemos optado por **convertir todas las imágenes en formato WebP**.

- El formato WebP es una alternativa más eficiente en comparación con formatos tradicionales como JPEG y PNG, ya que ofrece una mayor compresión sin perder calidad, lo que reduce el tiempo de carga de la página.
- Este cambio es especialmente importante cuando el proyecto escale o si más imágenes son añadidas en el futuro.

Para convertir imágenes a WebP, puedes usar herramientas como:
  - [Squoosh](https://squoosh.app/) (herramienta online)
  - [cwebp](https://developers.google.com/speed/webp) (herramienta de línea de comandos de Google)

### 🗃️ **Optimización del Código y Rendimiento**

Además del lazy loading de componentes y la optimización de imágenes, también se han implementado otras mejoras de rendimiento para garantizar una experiencia fluida y rápida:

- **Evitar la re-renderización innecesaria**: Se ha utilizado el sistema de reactividad de Vue.js para optimizar las actualizaciones de los componentes, reduciendo el costo computacional.
- **Reducción de dependencias no utilizadas**: Se ha eliminado cualquier dependencia que no se estuviera utilizando activamente en el proyecto, lo que reduce el tamaño total de los paquetes.

### ⚙️ **Optimización en la Conexión con la Base de Datos**

La API se conecta eficientemente con la base de datos para realizar operaciones CRUD de tareas. Se han realizado las siguientes optimizaciones en la capa del backend:

- **Optimización de las consultas SQL**: Se han utilizado filtros y limitaciones adecuadas en las consultas a la base de datos para evitar consultas innecesarias y mejorar la velocidad.
- **Implementación de validaciones y sanitización** de los datos en las entradas del formulario para prevenir **inyecciones SQL** y mejorar la seguridad de la aplicación.

## 📈 **Resultados Esperados de las Optimizaciónes**

Después de aplicar estas mejoras, se espera que el proyecto tenga un mejor rendimiento tanto en el **frontend** como en el **backend**. Las principales mejoras incluyen:

- Reducción de tiempos de carga inicial.
- Mejor experiencia de usuario, especialmente en dispositivos con redes lentas.
- Uso más eficiente de los recursos al cargar solo lo necesario en la página.
- Mayor seguridad mediante la validación y sanitización de datos.

---

¡Gracias por utilizar LUDIK! Si tienes alguna sugerencia o quieres contribuir con más mejoras, no dudes en abrir un **issue** o **pull request** en el repositorio. 🌟

### Explicación:

- **Lazy Loading de Componentes**: Se explica cómo se implementó el **lazy loading** en Vue.js, destacando el uso de `defineAsyncComponent` para cargar componentes de manera asincrónica.
  
- **Optimización de Imágenes**: El archivo menciona que, aunque no hay imágenes actualmente en el proyecto, se ha tomado en cuenta la optimización de imágenes para el futuro. Se menciona el uso del formato **WebP** para futuras imágenes, y se proporcionan algunas herramientas útiles para la conversión.

- **Optimización del Código**: Se incluyen mejoras generales en el código para optimizar la reactividad y eliminar dependencias no necesarias.

- **Optimización en la Conexión con la Base de Datos**: A nivel de backend, se menciona que se optimizaron las consultas y se implementaron prácticas de seguridad como la validación y sanitización de datos.

Este `README.md` explica de manera clara las optimizaciones realizadas en el proyecto, usando un tono amigable e informativo, adecuado para cualquier desarrollador que trabaje en el proyecto.