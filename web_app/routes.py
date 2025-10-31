from flask import render_template, get_flashed_messages
from web_app import app

@app.route('/')
def index():
    return render_template('index.html', title='Inicio')

@app.route('/generar')
def generar():
    return render_template('generar.html', title='Generar Claves')

@app.route('/firmar')
def firmar():
    return render_template('firmar.html', title='Firmar Documento')

@app.route('/verificar')
def verificar():
    return render_template('verificar.html', title='Verificar Firma')