import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import re
import json
import operator
from app.controllers.turma import Turma
from app.controllers.turma import Disciplina

class Aluno:
	""" Classe Aluno """

	turmasCursadas = []
	gradeHoraria = []

	def __init__(self, curso=None, turmasCursadas=None, gradeHoraria=None):
		"""Inicializador"""

		self.curso = curso
		self.turmasCursadas.append(turmasCursadas)
		self.gradeHoraria.append(gradeHoraria)

	def adicionarTurma(self, turma):
		"""Adiciona uma turma a lista de turmas do aluno"""

		self.turmasCursadas.append(turma)

	def removerTurma(self, codigo):
		"""Remove uma turma da lista com turmas do aluno"""
		x = None
		cont = 0
		for i in self.turmasCursadas:
			if i:
				if i.codigo == codigo:
					x = cont
					break
				cont += 1

		if x:
			del self.turmasCursadas[x]

	def consultarTurmas(self):
		"""Retorna uma lista com as turmas cursadas pelo aluno"""

		return self.turmasCursadas

	def consultarGradeHoraria(self):
		"""Retorna uma lista com a grade horaria do aluno"""

		return self.gradeHoraria

	def sugerirGradeHoraria(self):
		"""Algoritmo para sugestao de grade horaria"""

		ref = db.reference('/curso/' + self.curso)
		fluxo = ref.get()

		ref = db.reference('/trancamento/'+self.curso)
		grauTrancamento = ref.get()

		cursadas = {}
		for i in self.turmasCursadas:
			if i:
				for k in grauTrancamento:
					if k:
						for l in k:
							if i.codigo == l:
								k[l]['cursada'] = 1

		for k in grauTrancamento:
			if k:
				for l in k:
					if k[l]['cursada'] == 0:
						cursadas[l] = k[l]['grauTrancamento']
								

		cursadasOrdenadas = sorted(cursadas.items(), key=lambda x: x[1], reverse=True)

		for i in cursadasOrdenadas:
			turma = Disciplina()
			turma = self.buscarDisciplina(i[0])
			self.adicionarGradeHoraria(turma)

		return self.gradeHoraria

	def adicionarGradeHoraria(self, turma):
		"""Adiciona uma turma a lista de turmas do aluno"""

		self.gradeHoraria.append(turma)

	def buscarDisciplina(self, codigo):
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

	def checarCurso(self, curso):
		"""Algoritmo para verificacao do curso do arquivo PDF"""

		if re.match(r"ENGENHARIA DE SOFTWARE", curso):
			curso = "ENGENHARIA DE SOFTWARE"
		elif re.match(r"ARTES CÊNICAS", curso):
			curso = "ARTES CÊNICAS"
		elif re.match(r"ARTES VISUAIS", curso):
			curso = "ARTES VISUAIS"
		elif re.match(r"CIÊNCIA DA COMPUTAÇÃO", curso):
			curso = "CIÊNCIA DA COMPUTAÇÃO"
		elif re.match(r"CIÊNCIAS CONTÁBEIS", curso):
			curso = "CIÊNCIAS CONTÁBEIS"
		elif re.match(r"CIÊNCIAS NATURAIS", curso):
			curso = "CIÊNCIAS NATURAIS"
		elif re.match(r"COMPUTAÇÃO", curso):
			curso = "COMPUTAÇÃO"
		elif re.match(r"ENFERMAGEM", curso):
			curso = "ENFERMAGEM"
		elif re.match(r"ENGENHARIA AEROESPACIAL", curso):
			curso = "ENGENHARIA AEROESPACIAL"
		elif re.match(r"ENGENHARIA AUTOMOTIVA", curso):
			curso = "ENGENHARIA AUTOMOTIVA"
		elif re.match(r"ENGENHARIA DE COMPUTAÇÃO", curso):
			curso = "ENGENHARIA DE COMPUTAÇÃO"
		elif re.match(r"ENGENHARIA DE ENERGIA", curso):
			curso = "ENGENHARIA DE ENERGIA"
		elif re.match(r"ENGENHARIA ELETRÔNICA", curso):
			curso = "ENGENHARIA ELETRÔNICA"
		elif re.match(r"ENGENHARIA FLORESTAL", curso):
			curso = "ENGENHARIA FLORESTAL"
		elif re.match(r"ENGENHARIA MECÂNICA", curso):
			curso = "ENGENHARIA MECÂNICA"
		elif re.match(r"FARMÁCIA", curso):
			curso = "FARMÁCIA"
		elif re.match(r"FÍSICA", curso):
			curso = "FÍSICA"
		elif re.match(r"HISTÓRIA", curso):
			curso = "HISTÓRIA"
		elif re.match(r"LETRAS - LÍNGUA PORTUGUESA E RESPECTIVA LITERATURA", curso):
			curso = "LETRAS - LÍNGUA PORTUGUESA E RESPECTIVA LITERATURA"
		elif re.match(r"MÚSICA - FLAUTA", curso):
			curso = "MÚSICA - FLAUTA"
		elif re.match(r"RELAÇÕES INTERNACIONAIS", curso):
			curso = "RELAÇÕES INTERNACIONAIS"

		return curso