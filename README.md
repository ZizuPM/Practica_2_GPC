# Taller de Sistemas Operativos, Redes de Cómputo, Sistemas Distribuidos y Manejo de Información
![LOGO FC](https://github.com/ZizuPM/Practica1/blob/main/img_logoFC_2019.png)
# Practica II: _Código en repositorio en la nube y diferencia entre tráfico HTTP y HTTPS_.
![GCP_LOGO](https://github.com/ZizuPM/Practica_1_GPC/blob/main/gcp.png)
## Objetivo:
El alumno centralizará el código fuente de un proyecto web en la nube con Git (GitLab), adicionalmente visualizará la diferencia entre tráfico HTTP y HTTPS.

## Desarrollo
1.  Crea un *fork* del repositorio <https://gitlab.com/nehnemini/redes-2021-1>, en tu propia cuenta de Gitlab.
2.  Ingresa desde una terminal al servidor que instalaste en la Práctica 2, en AWS.
3.  Cambia al directorio `/var/www/html`.
4.  Clona tu repositorio creado en el paso 1, con el comando `sudo git clone <https://mi_repositorio>`.
5.  Cambia al directorio `/etc/apache2/sites-available/`.
6.  Copia el archivo `000-default.conf` al archivo `redesfc.conf`, utiliza la opción `-a` en el comando `cp`, para que se preserven los atributos del archivo, tales como el dueño, el grupo y los permisos.
7.  Con un editor de texto, abre el archivo `redesfc.conf` copiado en el paso anterior.
8.  Cambia el valor de la directiva `DocumentRoot`, en lugar de que esté establecido con la ruta `/var/www/html`, coloca la ruta en donde se encuentra el código HTML y otros elementos web de la carpeta `codigo_ejemplo/` de la práctica 3 del repositorio clonado en el punto 4. Por ejemplo, `/var/www/html/redes-2021-1/lab3/codigo_ejemplo`.
9.  Guarda los cambios en el archivo `redesfc.conf`
10. Cambia al directorio `/var/www/html`.
11. Cambia tanto el usuario como el grupo del directorio y de sus elementos, por tu usuario y grupo, por ejemplo `chown -R ubuntu:ubuntu redes-2021-1/`
12. En la terminal ejecuta el comando `sudo a2dissite 000-default.conf` para deshabilitar el sitio actual. Y ejecuta el comando `sudo a2ensite redesfc.conf`, para habilitar el nuevo sitio web. Para que se apliquen los cambios ejecuta reiniciar el servidor Apache, con el comando `sudo systemctl restart apache2.service`.
13. Ingresa desde un navegador web usando la dirección IP pública proporcionada por AWS (la *elastic IP*), al servidor web, y deberás visualizar el formulario. Además, ingresa a la ruta <http://mi_IP/images>, y observa el contenido.
14. En el mismo archivo `redesfc.conf`, agrega entre las directivas `<VirtualHost></VirtualHost>` lo siguiente. Verifica que la ruta del directorio para tu caso sea el correcto. Esto se usa para evitar que el servidor liste el contenido de los directorios de la ruta configurada en `DocumentRoot`, es una configuración de seguridad.

```
<Directory /var/www/html/redes-2021-1/lab3/codigo_ejemplo>
  Options -Indexes
</Directory>
```

15.  Para que se apliquen los cambios ejecuta `sudo systemctl restart apache2.service`.
16.  Ingresa de nuevo a la ruta <http://mi_IP/images>, y observa el cambio.
17.  Ejecuta el comando `sudo a2enmod cgid`, para habilitar el módulo de Apache de ejecución de CGI (*Common Gateway Interface*).
18.  En el mismo archivo `redesfc.conf`, agrega justo debajo de las líneas que se colocaron en el paso 14, las siguientes líneas para configurar la ejecución de scripts de Python en el directorio en donde está el repositorio de git. Verifica que la ruta del directorio para tu caso sea el correcto.

```
ScriptAlias /cgi-bin/ /var/www/html/redes-2021-1/lab3/codigo_ejemplo/cgi-bin/

<IfModule cgid_module>
    <Directory /var/www/html/redes-2021-1/lab3/codigo_ejemplo/cgi-bin/>
        Options -Indexes
        Options +ExecCGI
        AddHandler cgi-script .py
    </Directory>
</IfModule>
```

19.  Ingresa al formulario desde un navegador web, y verifica que se esté ejecutando correctamente el script de Python.
20.  Modifica la página web del formulario agregando una hoja de estilo, y al menos una imagen, colocando los archivos correspondiente en las carpetas destinadas para ello.
21.  Actualiza tu repositorio git cuando hayas aplicado los cambios.
22.  En tu equipo ejecuta Wireshark en la interfaz de red conectada a internet, y coloca un filtro para capturar sólo los mensajes que involucren la dirección IP de tu servidor o instancia en AWS, y en el puerto TCP/80.
23.  En un navegador web, consulta tu sitio, e ingresa un usuario y contraseña en el formulario, y da clic en el botón.
24.  En Wireshark, identifica y observa el mensaje en dónde se muestran en claro los datos que colocaste en el formulario, incluye la captura de pantalla de esto en tu reporte.
25.  Cambia tu formulario para que los datos se envíen por el método POST de HTTP, en lugar del método GET, recuerda reiniciar el servicio de Apache para evitar que la caché muestre el formulario anterior. Repite los pasos del 22 al 25.

## Guia para su desarrollo
