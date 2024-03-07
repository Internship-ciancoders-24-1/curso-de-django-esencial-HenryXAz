# Despliegue a producción de un proyecto Django

Primero es importante para desplegar nuestro proyecto el archivo wsgi.py. En el se específican las configuraciones necesarias del protocolo WSGI(Web Server Gateway Interface) y permite comunicar a un servidor web como nginx a nuestra aplicación escrita en python, de esta manera delegamos las tareas de procesamiento de peticiones al servidor web. Los archivos estáticos que vayan a servirse también formarán parte de las responsabilidades del servidor web.

Gunicorn es un servidor web que permite el despliegue de aplicaciones web creadas en python.

Para configurar la base de datos se debe de realizar dicha configuración en el archivo settings.py, precisamente en el diccionario 'DATABASES'. Django soporta múltiples bases de datos como pueden ser: mysql, postgresql, oracle, etc.

## Pasos para desplegar la aplicación

1. Actualización de los repositorios del sistema operativo(lo más común es utilizar un servidor con algún sistema operativo GNU/Linux)

2. Crear el usuario que va a ser propietario de los archivos del proyecto

3. Instalar en el sistema operativo todos los recursos necesarios. En el curso se utilizaron los siguientes recursos para poder desplegar la aplicación:
    
    * Python3
    * Nginx
    * Git
    * Postgresql
    * Gunicorn

3. Clonar el repositorio

4. En el archivo settings.py del proyecto de django agregar la dirección de dominio de la aplicación en la lista denominada 'ALLOWED_HOSTS'

5. Configurar un archivo nginx que será el servidor web que recibirá todas las peticiones. El archivo deberá tener una estructura similar a la siguiente:

```nginx
upstream django_app {
server 127.0.0.1:8000;
}
server {
listen 80;
server_name demo.gatos.io;
access_log /var/log/nginx/app.log;
error_log /var/log/nginx/app.error.log;
location /static {
autoindex on;
alias /home/platzi/platzi/staticfiles/;
}
location /media {
autoindex on;
alias /home/platzi/platzi/media/;
}
location / {
proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
proxy_set_header Host $http_host;
proxy_redirect off;
proxy_pass http://django_app;
}
}
```

6. Crear un script que ejecutará instrucciones de gunicorn y darle permisos de ejecución con el comando chmod +x <nombre del script>

7. Crear un servicio de init que ejecute el script de gunicorn creado anteriormente. Para esto se debe de realizar lo siguiente:

    * Ejecutar ```bash sudo su``` para tener permisos de administrador(nos pedirá contraseña y es necesario que nuestro usuario este agregado al archivo sudoers)

    * Ir a la carpeta /etc/init ejecutando el comando ```bash cd /etc/init```

    * Crear un archivo con extensión .conf como por ejemplo 'my_app.conf'. El archivo se crea con el comando ```bash touch my_app.conf```

    * el archivo deberá contener instrucciones similares a las siguientes:

    ```text
    start on startup
    script
    exec /home/my_app/deploy/gunicorn_start
    end script
    ```
8. Iniciar el servicio con el comando ```bash service my_app start```

9. Por último se debe de ejecutar el siguiente comando ```bash ./manage.py collectstatic```