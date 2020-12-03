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

def buscarDisciplina(codigo):
	campus = codigo[:3]

	# Referencia a no do banco de dados
	ref = db.reference('/disciplina/' + campus + '/' + codigo)
	disciplinas = ref.get()

	if disciplinas:
		turma = Turma()
		turma.codigo = codigo

		# adiciona o nome e a carga horaria da disciplina na lista, por esta presente em todas as disciplinas nao e feita a verificacao da existencia dos dados
		turma.nome = disciplinas['nome']
		turma.cargaHoraria = disciplinas['cargaHoraria']

		# verifica se a disciplina tem ementa disponivel e a adiciona na lista
		if 'ementa' in disciplinas:
			turma.ementa = disciplinas['ementa']
		else:
			turma.ementa = 'Indisponivel'

		if 'preRequisitos' in disciplinas:
			turma.preRequisitos = disciplinas['preRequisitos']
		else:
			turma.preRequisitos = 'Indisponivel'

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

		return turma

@app.route("/disciplina", methods=["GET", "POST"])
@cross_origin(supports_credentials=True)
def disciplina():
	getData = request.get_json()
	turma = Turma()
	if getData:
		turma = buscarDisciplina(getData)
	return turma.getTurma()

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
