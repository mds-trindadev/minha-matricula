from app import app
from flask import Flask, request, render_template

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

from app.controllers.turma import Turma
from app.controllers.turma import Disciplina
from app.controllers.aluno import Aluno
from app.controllers.semestre import Semestre
from app.controllers.curso import Curso

cred = credentials.Certificate(r"./app/controllers/serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://minha-matricula.firebaseio.com/'
})

# LISTA DE DEPARTAMENTOS:
# ADM, BOT, CCA, CDS, CDT, CEL, CEM, CEN, CET, CFS, CIC, CID, COM, COT, DAN, DAP, DEG, DEX, DIN, DSC, ECL, ECO, 
# EFL, ELA, ENC, ENE, ENF, ENM, EPR, EST, FAC, FAR, FAU, FAV, FCE, FCI, FCS, FDD, FEA, FED, FEF, FGA, FIL, FIT, 
# FMD, FTD, FUP, GEA, GEM, GPP, HIS, ICB, ICH, IDA, IFD, IGD, ILD, IPD, IQD, IRI, JOR, LET, MAT, MUS, NUT, ODT, 
# PAD, PCL, PRO, SER, SOL, TAU, TEC, TEL, VIS, ZOO

nomeDepartamento = 'FGA'

@app.route("/")
def home():
	# Referencia a no do banco de dados
	ref = db.reference('/disciplina/' + nomeDepartamento)
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

		turma = Turma()
		# adiciona o codigo da disciplina na lista
		turma.codigo = codigo
		info = ref.child(codigo).get()
		
		# adiciona o nome e a carga horaria da disciplina na lista, por esta presente em todas as disciplinas nao e feita a verificacao da existencia dos dados
		turma.nome = info['nome']
		turma.cargaHoraria = info['cargaHoraria']

		# verifica se a disciplina tem ementa disponivel e a adiciona na lista
		if 'ementa' in info:
			turma.ementa = info['ementa']

		# percorre as turmas disponiveis na disciplina
		if 'turmas' in info:
			for i in info['turmas']:
				# adiciona as informacoes referentes a turma na lista
				turma.sigla = info['turmas'][i]
				turma.periodo = info['turmas'][i]['periodo']
				turma.professor = info['turmas'][i]['professor']
				if 'horario' in info['turmas'][i]:
					turma.horario = info['turmas'][i]['horario']

				data.append(turma)

	# chama a View e passa a lista "data" como parametro
	return render_template('home.html', data=data)