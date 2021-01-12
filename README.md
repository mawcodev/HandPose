# HandPose
Este proyecto reconoce la posición de las manos, es decir, los gestos que hace la mano, en este identificaremos solo 
algunos de ellos.

## Modelos tensorflow

### 1. Instalación tensorflow

```
pip install tensorflow
```

### 2. Carga de los modelos

Dentro del fichero .py que nosostros vayamos ha asignar para dicho cometido:

```
import * as handpose from '@tensorflow-models/handpose';
import * as tf from '@tensorflow/tfjs-core';
import * as tfjsWasm from '@tensorflow/tfjs-backend-wasm';
import '@tensorflow/tfjs-backend-webgl';
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

## Activamos el modo debug

Para activar el modo debug en flask debemos ejecutar, en este caso Windows, los siguientes comandos:

```
set FLASK_ENV=development
set FLASK_DEBUG=1
```
Si queremos volver al modo de producción cambiamos los anteriores parametros por `production` y `0`, respectivamente.

Espero que les haya servido de ayuda!

Ahora vamos a añadir el modelo de HandPose.