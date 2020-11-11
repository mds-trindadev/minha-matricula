from app import app
from flask import Flask, request, render_template

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate(r"./app/controllers/serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://minha-matricula.firebaseio.com/'
})

# LISTA DE DEPARTAMENTOS JA REVISADOS:
# ADM, BOT, CCA, CDS, CDT, CEL, CEM, CEN, CET, CFS, CIC, CID, COM, COT, DAN, DAP, DEG, DEX, DIN, DSC, FGA
nomeDepartamento = 'FGA'

@app.route("/")
def home():
	# Referencia a no do banco de dados
	ref = db.reference('/'+nomeDepartamento)
	cont = 0

	# Lista que armazena dados
	data = []

	# Pega os dados do banco
	disciplinas = ref.get()

	# Percorre dicionario
	for codigo in disciplinas:
		# contador de parada para nao percorrer todas as disciplinas
		cont += 1
		if cont > 3:
			break

		# adiciona o codigo da disciplina na lista
		data.append('Codigo: ' + codigo)
		info = ref.child(codigo).get()
		
		# adiciona o nome e a carga horaria da disciplina na lista, por esta presente em todas as disciplinas nao e feita a verificacao da existencia dos dados
		data.append(info['nome'])
		data.append(info['cargaHoraria'])

		# verifica se a disciplina tem ementa disponivel e a adiciona na lista
		if 'ementa' in info:
			data.append(info['ementa'])

		# percorre as turmas disponiveis na disciplina
		if 'turmas' in info:
			for i in info['turmas']:
				# adiciona as informacoes referentes a turma na lista
				data.append(info['turmas'][i]['periodo'])
				data.append(info['turmas'][i]['professor'])
				if 'horario' in info['turmas'][i]:
					data.append(info['turmas'][i]['horario'])

	# chama a View e passa a lista "data" como parametro
	return render_template('home.html', data=data)