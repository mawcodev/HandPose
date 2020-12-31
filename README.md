# HandPose
This proyect is recognition hand pose with flask framework and python

## Instalación Flask

### 1. Creación del virtualenv

Una vez instalado Python, necesitamos crear una ventana de trabajo, instalamos virtualenv con pip o pip3, dependiendo de nuestra versión.
Si estamos en Windows desde la CMD y dentro del repositorio que deseemos crear la ventana de trabajo escribimos:

```
python -m virtualenv env
```
Esto crea el directorio `env`.

### 2. Activación ventana de trabajo

Para trabajar en esta ventana virtual la activamos, en mi caso desde Windows con CMD:

```
env\Scripts\activate.bat
```
Ahora vamos a instalar el framework, en este caso se utiliza Flask.

### 3. Instalación de Flask

Lo instalamos dentro del entorno de trabajo, observaremos que está activo si delante de la ruta tenemos `(env)`.
Seguidamente instalamos el framework.

```
pip3 install Flask
```

Sí quereís comprobar si se ha instalado correctamente podeís ver las distintas dependencias que teneís instaladas con:

```
pip3 freeze
```
## Creando la aplicación

Creación de un fichero llamado `app.py`

Añadiremos un código de prueba. Donde, llamaremos a la clase de Flask e instanciamos para que Flask sepa donde encontrar los ficheros estáticos de nuestra aplicación.

```
from flask import Flask
app = Flask(__name__)
```
Creamos `route`, encargado de decir a Flask qué URL debe ejecutar.

```
@app.route('/')
```
Por último, creamos una función de prueba:

```
def new_year():
    return 'Happy New Year!'
```
### Ejecutamos la app

Antes de ejecutar la aplicación debemos indicarle al servidor qué aplicación debe ejecutar declarando la variable de entorno `FLASK_APP`.

En Windows, vamos al fichero `env\Scripts\activate.bat` y al final del fichero añadimos `set "FLASK_APP=app.py"`. Salimos del entorno con `env\Scripts\deactivate.bat` y volvemos a entrar en el entorno `env`.

Ejecutamos:

```
python -m flask run
```