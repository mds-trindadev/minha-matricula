import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import re

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
<<<<<<< HEAD

	def extrairDadosPDF(self):
		"""Algoritmo para extracao dos dados do arquivo PDF"""

		############## FALTA IMPLEMENTAR
=======
		return self.gradeHoraria

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
>>>>>>> backend
