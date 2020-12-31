"""
Fichero: app.py
Descripción: El corazón de la aplicación. Fichero que se lanza al querer iniciar la aplicación.
Autor: Matthew Conde Oltra
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')

def happy_new_year():
    return 'Happy new year! By @Mawconol'