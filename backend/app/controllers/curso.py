class Curso:
	""" Classe Curso """

	curso = []

	def __init__(self, duracao, semestre):
		"""Inicializador"""

		self.duracao = duracao
		self.curso.append(semestre)

	def getCurso(self):
		"""Retorna um dicionario com informacoes referentes ao curso"""

		return {'duracao': self.duracao, 'curso': self.curso}