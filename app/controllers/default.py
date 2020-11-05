from app import app
from flask import Flask, request, render_template

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate(r"./app/controllers/serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://minha-matricula.firebaseio.com/'
})

ref = db.reference('/')

@app.route("/")
def home():
	ref = db.reference('FGA')
	data = ref.get()
	return render_template('home.html', data=data)