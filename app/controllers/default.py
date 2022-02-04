from flask import render_template, redirect
from app import app


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/galeria")
def galeria():
    return render_template('galeria.html')

@app.route("/sobrenos")
def sobrenos():
    return render_template('sobreNos.html')

@app.route("/contacto")
def contacto():
    return render_template('contacto.html')
