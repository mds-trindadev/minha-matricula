import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate(r"./app/controllers/serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://minha-matricula.firebaseio.com/'
})

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

	def sugerirGradeHoraria(self, fluxo):
		"""Algoritmo para sugestao de grade horaria"""

		############## FALTA IMPLEMENTAR
		return self.gradeHoraria

	def extrairDadosPDF(self):
		"""Algoritmo para extracao dos dados do arquivo PDF"""

		############## FALTA IMPLEMENTAR