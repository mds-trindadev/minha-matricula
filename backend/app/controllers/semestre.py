class Semestre:
	""" Classe Semestre """

	codigoDisciplinas = []

	def __init__(self, periodo, codigoDisciplina):
		"""Inicializador"""

		self.periodo = periodo
		self.codigoDisciplinas.append(codigoDisciplina)

	def getSemestre(self):
		"""Retorna um dicionario com informacoes referentes ao semestre"""

		return {'periodo': self.periodo, 'codigoDisciplinas': self.codigoDisciplinas}

	def addCodigoDisciplina(self, codigoDisciplina):
		"""Adiciona uma disciplina ao semestre"""

		self.codigoDisciplinas.append(codigoDisciplina)