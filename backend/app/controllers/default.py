from app import app
from flask import Flask, request, render_template, jsonify
from flask_jwt_extended import JWTManager

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

from app.controllers.turma import Turma
from app.controllers.turma import Disciplina
from app.controllers.aluno import Aluno
from app.controllers.semestre import Semestre
from app.controllers.curso import Curso

from flask_cors import CORS, cross_origin

CORS(app, support_credentials=True)
JWTManager(app)

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
aluno = Aluno()

@app.route("/pesquisa", methods=["GET", "POST"])
@cross_origin(supports_credentials=True)
def pesquisa():
	getData = request.get_json()
	
	# Lista que armazena dados
	data = {}

	if getData:
		#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
		#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
		# ARRUMAR AQUI
		campus = getData.get("campus")
		if getData.get("campus") == "unb":
			campus = "FAC"

		# Referencia a no do banco de dados
		ref = db.reference('/disciplina/' + campus)
		cont = 0

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
			
			# verifica se o nome da materia corresponde a pesquisa
			if(info['nome'] != getData.get("nome")):
				continue

			# adiciona o nome e a carga horaria da disciplina na lista, por esta presente em todas as disciplinas nao e feita a verificacao da existencia dos dados
			turma.nome = info['nome']
			turma.cargaHoraria = info['cargaHoraria']

			# verifica se a disciplina tem ementa disponivel e a adiciona na lista
			if 'ementa' in info:
				turma.ementa = info['ementa']
			else:
				turma.ementa = info['Indisponivel']

			if 'preRequisitos' in info:
				turma.preRequisitos = info['preRequisitos']
			else:
				turma.preRequisitos = info['Indisponivel']

			# percorre as turmas disponiveis na disciplina
			if 'turmas' in info:
				for i in info['turmas']:
					# adiciona as informacoes referentes a turma na lista
					turma.sigla = info['turmas']
					turma.periodo = info['turmas'][i]['periodo']
					turma.professor = info['turmas'][i]['professor']
					if 'horario' in info['turmas'][i]:
						turma.horario = info['turmas'][i]['horario']
					else:
						turma.horario = 'Indisponivel'
			else:
				turma.ementa = 'Indisponivel'
				turma.sigla = 'Indisponivel'
				turma.periodo = 'Indisponivel'
				turma.professor = 'Indisponivel'
				turma.horario = 'Indisponivel'

			temp = turma.getTurma()
			if(temp['creditos'] == getData.get("creditos")):
				data[turma.codigo] = temp

	return data

@app.route("/disciplina", methods=["GET", "POST"])
@cross_origin(supports_credentials=True)
def disciplina():
	getData = request.get_json()

	data = ''
	if getData:
		campus = getData.get("codigo")[:3]

		# Referencia a no do banco de dados
		ref = db.reference('/disciplina/' + campus + '/' + getData.get("codigo"))
		disciplinas = ref.get()

		turma = Turma()
		turma.codigo = disciplinas

		# adiciona o nome e a carga horaria da disciplina na lista, por esta presente em todas as disciplinas nao e feita a verificacao da existencia dos dados
		turma.nome = disciplinas['nome']
		turma.cargaHoraria = disciplinas['cargaHoraria']

		# verifica se a disciplina tem ementa disponivel e a adiciona na lista
		if 'ementa' in disciplinas:
			turma.ementa = disciplinas['ementa']
		else:
			turma.ementa = disciplinas['Indisponivel']

		if 'preRequisitos' in disciplinas:
			turma.preRequisitos = disciplinas['preRequisitos']
		else:
			turma.preRequisitos = disciplinas['Indisponivel']

		# percorre as turmas disponiveis na disciplina
		if 'turmas' in disciplinas:
			for i in disciplinas['turmas']:
				# adiciona as informacoes referentes a turma na lista
				turma.sigla = disciplinas['turmas']
				turma.periodo = disciplinas['turmas'][i]['periodo']
				turma.professor = disciplinas['turmas'][i]['professor']
				if 'horario' in disciplinas['turmas'][i]:
					turma.horario = disciplinas['turmas'][i]['horario']
				else:
					turma.horario = 'Indisponivel'
		else:
			turma.ementa = 'Indisponivel'
			turma.sigla = 'Indisponivel'
			turma.periodo = 'Indisponivel'
			turma.professor = 'Indisponivel'
			turma.horario = 'Indisponivel'

		data = turma.getTurma()
				
	return data

@app.route("/gradeHoraria", methods=["GET", "POST"])
@cross_origin(supports_credentials=True)
def gradeHoraria():
	return jsonify({ "data" : "GradeHoraria" })

		data = turma.getTurma()
				
	return data

@app.route("/gradeHoraria", methods=["GET", "POST"])
@cross_origin(supports_credentials=True)
def gradeHoraria():
	getData = request.get_json()

	if getData:
		if getData.get("op") == 'setCurso':
			aluno.curso = getData.get("curso")
			return { 'status': 'Success'}

		elif getData.get("op") == 'addDisciplina':
			turma = Turma()

			turma.codigo = getData.get("codigoDisciplina")
			turma.nome = getData.get("nomeDisciplina")
			turma.cargaHoraria = getData.get("cargaHorariaDisciplina")
			turma.ementa = getData.get("ementaDisciplina")
			turma.preRequisitos = getData.get("preRequisitosDisciplina")
			turma.concluida = True
			if getData.get("siglaDisciplina"):
				turma.sigla = getData.get("siglaDisciplina")
				turma.periodo = getData.get("periodoDisciplina")
				turma.professor = getData.get("professorDisciplina")
				turma.horario = getData.get("horarioDisciplina")
			
			aluno.adicionarTurma(turma)
			return { 'status': 'Success'}

		elif getData.get("op") == 'rmDisciplina':
			aluno.removerTurma(getData.get("codigoDisciplina"))
			return { 'status': 'Success'}

		elif getData.get("op") == 'getTurmas':
			data = {}
			for i in aluno.consultarTurmas():
				if i:
					data[i.codigo] = i.getTurma()

			return data

		elif getData.get("op") == 'getGradeHoraria':
			data = {}
			for i in aluno.consultarGradeHoraria():
				if i:
					data[i.codigo] = i.getTurma()

			return data

		elif getData.get("op") == 'sugerirGradeHoraria':
			data = {}

			ref = db.reference('/curso/' + aluno.curso)
			fluxo = ref.get()


			for i in aluno.consultarGradeHoraria(fluxo):
				if i:
					data[i.codigo] = i.getTurma()

			return data

		else:
			return { 'status': 'Fail'}
