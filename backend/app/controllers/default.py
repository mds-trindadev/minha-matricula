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
from app.controllers.prioridade_materia import Graph

from flask_cors import CORS, cross_origin

from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.converter import TextConverter
import io
import camelot
import re
import sys
import json
import os

import pikepdf
from random import randint

if not os.path.exists('./uploads'): os.makedirs('./uploads')\

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
			temp = Disciplina()
			# adiciona o codigo da disciplina na lista
			temp.codigo = codigo
			info = ref.child(codigo).get()
			
			# verifica se o nome da materia corresponde a pesquisa
			if(info['nome'] != getData.get("nome")):
				continue

			# adiciona o nome e a carga horaria da disciplina na lista, por esta presente em todas as disciplinas nao e feita a verificacao da existencia dos dados
			temp.nome = info['nome']
			temp.departamento = temp.codigo[:3]
			temp.cargaHoraria = info['cargaHoraria']

			# verifica se a disciplina tem ementa disponivel e a adiciona na lista
			if 'ementa' in info:
				temp.ementa = info['ementa']
			else:
				temp.ementa = 'Indisponivel'

			if 'preRequisitos' in info:
				temp.preRequisitos = info['preRequisitos']
			else:
				temp.preRequisitos = 'Indisponivel'

			# percorre as turmas disponiveis na disciplina
			if 'turmas' in info:
				for i in info['turmas']:
					tempTurma = Turma()
					# adiciona as informacoes referentes a turma na lista
					tempTurma.turma = i
					tempTurma.periodo = info['turmas'][i]['periodo']
					tempTurma.professor = info['turmas'][i]['professor']
					if 'horario' in info['turmas'][i]:
						tempTurma.horario = info['turmas'][i]['horario']
					else:
						tempTurma.horario = 'Indisponivel'

					temp.addTurma(tempTurma)
			else:
				tempTurma = Turma()
				tempTurma.turma = 'Indisponivel'
				tempTurma.periodo = 'Indisponivel'
				tempTurma.professor = 'Indisponivel'
				tempTurma.horario = 'Indisponivel'

				temp.addTurma(tempTurma)

			temp = temp.getDisciplina()
			if(temp['creditos'] == getData.get("creditos")):
				data[temp['codigo']] = temp

	return data

def buscarDisciplina(codigo):
	campus = codigo[:3]

	# Referencia a no do banco de dados
	ref = db.reference('/disciplina/' + campus + '/' + codigo)
	disciplinas = ref.get()

	if disciplinas:
		temp = Disciplina()
		
		# adiciona o codigo da disciplina na lista
		temp.codigo = codigo
		temp.departamento = campus
			
		# adiciona o nome e a carga horaria da disciplina na lista, por esta presente em todas as disciplinas nao e feita a verificacao da existencia dos dados
		temp.nome = disciplinas['nome']
		temp.cargaHoraria = disciplinas['cargaHoraria']

		# verifica se a disciplina tem ementa disponivel e a adiciona na lista
		if 'ementa' in disciplinas:
			temp.ementa = disciplinas['ementa']
		else:
			temp.ementa = 'Indisponivel'

		if 'preRequisitos' in disciplinas:
			temp.preRequisitos = disciplinas['preRequisitos']
		else:
			temp.preRequisitos = 'Indisponivel'

		# percorre as turmas disponiveis na disciplina
		if 'turmas' in disciplinas:
			for i in disciplinas['turmas']:
				tempTurma = Turma()
				# adiciona as informacoes referentes a turma na lista
				tempTurma.turma = i
				tempTurma.periodo = disciplinas['turmas'][i]['periodo']
				tempTurma.professor = disciplinas['turmas'][i]['professor']
				if 'horario' in disciplinas['turmas'][i]:
					tempTurma.horario = disciplinas['turmas'][i]['horario']
				else:
					tempTurma.horario = 'Indisponivel'

				temp.addTurma(tempTurma)
		else:
			tempTurma = Turma()
			tempTurma.turma = 'Indisponivel'
			tempTurma.periodo = 'Indisponivel'
			tempTurma.professor = 'Indisponivel'
			tempTurma.horario = 'Indisponivel'
			temp.addTurma(tempTurma)

		return temp

@app.route("/disciplina", methods=["GET", "POST"])
@cross_origin(supports_credentials=True)
def disciplina():
	getData = request.get_json()
	turma = Disciplina()
	if getData:
		turma = buscarDisciplina(getData['codigo'])

	return turma.getDisciplina()

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
			temp = Disciplina()

			temp.codigo = getData.get("codigoDisciplina")
			temp.nome = getData.get("nomeDisciplina")
			temp.cargaHoraria = getData.get("cargaHorariaDisciplina")
			temp.ementa = getData.get("ementaDisciplina")
			temp.concluida = True

			temp.preRequisitos = ''
			if getData.get("preRequisitosDisciplina"):
				for i in getData.get("preRequisitosDisciplina"):
					temp.preRequisitos = temp.preRequisitos + ' ' + getData.get("preRequisitosDisciplina")[i]

			if getData.get("turmasDisciplina"):
				tempTurma = Turma()
				for i in getData.get("turmasDisciplina"):
					t = json.loads(getData.get("turmasDisciplina")[i].replace("'", '"').replace("None", '"None"'))
					tempTurma.turma = t["turma"]
					tempTurma.periodo = t["periodo"]
					tempTurma.professor = t["professor"]
					tempTurma.horario = t["horario"]

					temp.addTurma(tempTurma)

			aluno.adicionarTurma(temp)
			return { 'status': 'Success'}

		elif getData.get("op") == 'rmDisciplina':
			aluno.removerTurma(getData.get("codigoDisciplina"))
			return { 'status': 'Success'}

		elif getData.get("op") == 'getTurmas':
			data = {}
			for i in aluno.consultarTurmas():
				if i:
					data[i.codigo] = i.getDisciplina()

			return data

		elif getData.get("op") == 'getGradeHoraria':
			data = {}
			for i in aluno.consultarGradeHoraria():
				if i:
					data[i.codigo] = i.getDisciplina()

			return data

		elif getData.get("op") == 'sugerirGradeHoraria':
			data = {}
			aluno.sugerirGradeHoraria()
			return { 'status': 'Success'}

		else:
			return { 'status': 'Fail'}

def acceptable_file(file_name):
	if re.findall("[.]", file_name):
		return True
	else:
		return False

def extract_text(pdf_path):
	resource_manager = PDFResourceManager()
	fake_file_handle = io.StringIO()
	converter = TextConverter(resource_manager, fake_file_handle)
	page_interpreter = PDFPageInterpreter(resource_manager, converter)

	with open(pdf_path, 'rb') as fh:
		for page in PDFPage.get_pages(fh, caching=True, check_extractable=True):
			page_interpreter.process_page(page)

	text = fake_file_handle.getvalue()

	converter.close()
	fake_file_handle.close()

	if text:
		return text

def get_info(text):
	return {
		"curso": re.search(r"(?<=Dados do Vínculo do Discente)(.*)(?=[0-9]{4}\.[0-9]\s/)", text).group()
	}


def get_table(file_name):
	return camelot.read_pdf(file_name)[0].df

@app.route('/upload', methods=['GET', 'POST'])
def upload():
	if request.method == 'POST':
		nomeAleatorio = str(randint(0,100000))

		request_data = request.get_data()
		with open('./uploads/file'+nomeAleatorio+'.pdf', 'wb') as wf:
			wf.write(request_data)

		with pikepdf.open('./uploads/file'+nomeAleatorio+'.pdf') as pdf:
			pdf.save('./uploads/temp_file'+nomeAleatorio+'.pdf')

		os.remove('./uploads/file'+nomeAleatorio+'.pdf')
		file_path = './uploads/temp_file'+nomeAleatorio+'.pdf'
		pdf_text = extract_text(file_path)
		user_data = get_info(pdf_text)
		pdf_table = get_table(file_path)
		data = user_data
		data["componentes"] = []

		for row in pdf_table.drop(0).itertuples():
			componente = {
				"codigo": row[3],
				"situacao": row[9],
			}
			data["componentes"].append(componente)
		os.remove('./uploads/temp_file'+nomeAleatorio+'.pdf')

		for componente in data["componentes"]:
			if len(componente["codigo"]) == 7 and componente["situacao"] == "APR":
				turma = buscarDisciplina(componente["codigo"])
				if turma:
					turma.concluida = True
					aluno.adicionarTurma(turma)

		aluno.curso = aluno.checarCurso(data["curso"])
		
		return { 'status': 'Success'}

	return { 'status': 'Fail'}

@app.route('/fluxo', methods=['GET', 'POST'])
def fluxo():
	getData = request.get_json()
	ref = db.reference('/curso/' + getData.get("curso"))
	fluxo = ref.get()
	n = 1
	dictFluxo = {}
	for i in fluxo:
		if i:
			dictFluxo[n] = i
			n += 1
	return dictFluxo

# @app.route('/bancoDados', methods=['GET', 'POST'])
# def bancoDados():
# 	prioridade = Graph(100)
# 	prioridade.buscarBancodeDados()