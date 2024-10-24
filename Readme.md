# Prueba Tecnica 

En este proyecto se encuentra la automatización del registro, inicio de sesion y cerrado de sesion de la pagina "https://test-qa.inlaze.com/auth/sign-in" en esta hay un total de 7 carpetas organizadas y con el siguiente contenido.

## CONTENIDO

El proyecto contine 7 carpetas, el las cuales se encuentra:

* data.py: Dentro de este se almacena la información que se enviara en las solicitudes, así mismo las configuraciones para el proyecto en donde se almacenan la ruta al servidor.


* Pages.py: Dentro de esta se encuentran los localizadores de las funciones relacionadas con las distintas páginas de la aplicación, estas estan ordenadas de la siguiente forma 
  - SignUP: Clase encargada de realizar el registro de un nuevo usuario.
  - Login: Clase para gestionar el inicio de sesión de un usuario.
  - Logout: Clase para gestionar el cierre de sesión del usuario.


* main.py: Dentro de este se encuentra las pruebas para realizar el registro, el ingreso y la salida del usuario, estas se encuentran ordenadas de la siguente manera
  - TestUser: Contiene los casos de prueba:
    * test_signup: Verifica el flujo de registro.
    * test_login: Verifica que el usuario pueda iniciar sesión correctamente.
    * test_logout: Verifica que el usuario pueda cerrar sesión.


* Nameinvalid.py: Se encuentra organizada que la carpeta main solo que en esta el test_signup: se encuentra modificado para el que el nombre sea invalido y así ver si permite crear el registro


* Emailinvalid: Esta carpeta es igual que la anterior nombrada el cambio es que en esta tambien se encuentra diferente el test_login, modificado para evaluar si permite el ingreso de un email no valido.


* Passwordinvalid:Esta carpeta es igual que la anterior nombrada el cambio es que en esta tambien se encuentra diferente el test_login, modificado para evaluar si permite el ingreso de una contraseña no valida.


* README.md: El cual guarda la descripción del proyecto.


* gitignore: En este se guardan archivos para que Git los descarte


## Tecnologías utilizadas:
- Herramienta de Automatización: Selenium y pytest
- Lenguaje de programación: Python
- Entorno de Pruebas: Navegador Chrome

### Descargas 

1. Descarga de python
2. Descarga de Pytest desde PyCharm
3. Descarga de Git
4. Descarga de paquete selenium, desde el comando pip install
5. Descarga de paquete request, desde el comando pip install
6. Instalación de ChromeDriver


Todas estas pruebas se realizaron en Chrome version 130.0.6723.60 (Build oficial) (64 bits)


