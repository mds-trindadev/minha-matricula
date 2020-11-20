class Aluno:
	""" Classe Aluno """

	turmasCursadas = []
	gradeHoraria = []

	def __init__(self, curso, turmasCursadas=None, gradeHoraria=None):
		"""Inicializador"""

		self.curso = curso
		self.turmasCursadas.append(turmasCursadas)
		self.gradeHoraria.append(gradeHoraria)

	def adicionarTurma(self, turma):
		"""Adiciona uma turma a lista de turmas do aluno"""

		self.turmasCursadas.append(turma)

	def removerTurma(self, indice):
		"""Remove uma turma da lista com turmas do aluno"""

		del self.turmasCursadas[indice]

	def consultarTurmas(self):
		"""Retorna uma lista com as turmas cursadas pelo aluno"""

		return self.turmasCursadas

	def consultarGradeHoraria(self):
		"""Retorna uma lista com a grade horaria do aluno"""

		return self.gradeHoraria

	def sugerirGradeHoraria(self):
		"""Algoritmo para sugestao de grade horaria"""

	def extrairDadosPDF(self):
		"""Algoritmo para extracao dos dados do arquivo PDF"""