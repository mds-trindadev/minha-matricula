import re

class Departamento:
	""" Classe Departamento """

	def __init__(self, codigo):
		"""Inicializador"""

		self.codigo = codigo

	def getDepartamento(self):
		"""Retorna o codigo do departamento"""

		return self.codigo

class Disciplina(Departamento):
	""" Classe Disciplina """

	def __init__(self, codigo=None, nome=None, ementa=None, preRequisitos=None, cargaHoraria=None, departamento=None, campus=None):
		"""Inicializador"""

		Departamento.__init__(self, codigo)
		self.nome = nome
		self.ementa = ementa
		self.preRequisitos = preRequisitos
		self.cargaHoraria = cargaHoraria
		self.creditos = 0
		self.prioridade = 0
		self.concluida = False
		self.campus = campus
		self.departamento = departamento
		self.vetorTurma = []

	def getDisciplina(self):
		"""Retorna um dicionario com as informacoes referentes a disciplina"""

		self.creditos = int(re.findall(r'\d+', str(self.cargaHoraria))[0])/15

		if self.departamento == 'FGA':
			self.campus = 'FGA'
		elif self.departamento == 'FCE':
			self.campus = 'FCE'
		elif self.departamento == 'FUP':
			self.campus = 'FUP'
		else:
			self.campus = 'Darcy Ribeiro'

		dictTurmas = {}
		n = 0;
		for i in self.vetorTurma:
			dictTurmas[n] = i.getTurma()
			n += 1

		return {
				'codigo': self.codigo,
				'nome': self.nome, 
				'ementa': self.ementa, 
				'preRequisitos': self.preRequisitos,
				'cargaHoraria': self.cargaHoraria,
				'creditos': self.creditos,
				'prioridade': self.prioridade,
				'concluida': self.concluida,
				'campus': self.campus,
				'departamento': self.departamento,
				'turmas': dictTurmas
				}

	def addTurma(self, turma):
		"""Adiciona novas turmas"""

		self.vetorTurma.append(turma)

class Turma(Disciplina):
	""" Classe Turma """

	def __init__(self, turma=None, horario=None, professor=None, periodo=None):
		"""Inicializador"""

		self.turma = turma
		self.horario = horario
		self.professor = professor
		self.periodo = periodo

	def getTurma(self):
		"""Retorna um dicionario com as informacoes referentes a turma"""

		return {
				'turma': self.turma,
				'horario': self.horario,
				'professor': self.professor,
				'periodo': self.periodo
				}