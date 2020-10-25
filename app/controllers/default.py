# import firebase_admin
# import pyrebase
# import json
from app import app
# from firebase_admin import credentials, auth
from flask import Flask, request, render_template

@app.route("/")
@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/cadastro")
def cadastro():
    return render_template('cadastro.html')

@app.route("/esqueceu")
def esqueceu():
    return render_template('esqueceu.html')

@app.route("/perfil")
def perfil():
    return render_template('perfil.html')