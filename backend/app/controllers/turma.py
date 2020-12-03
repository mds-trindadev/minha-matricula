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

	def __init__(self, codigo, nome, ementa, preRequisitos, cargaHoraria):
		"""Inicializador"""

		Departamento.__init__(self, codigo)
		self.nome = nome
		self.ementa = ementa
		self.preRequisitos = preRequisitos
		self.cargaHoraria = cargaHoraria
		self.creditos = 0
		self.prioridade = 0
		self.concluida = False

	def getDisciplina(self):
		"""Retorna um dicionario com as informacoes referentes a disciplina"""

		self.preRequisitos = re.findall(r'[A-Z]{3}[0-9]{4}', self.preRequisitos)
		self.creditos = int(re.findall(r'\d+', str(self.cargaHoraria))[0])/15

		return {
				'codigo': self.codigo,
				'nome': self.nome, 
				'ementa': self.ementa, 
				'preRequisitos': self.preRequisitos,
				'cargaHoraria': self.cargaHoraria,
				'creditos': self.creditos,
				'prioridade': self.prioridade,
				'concluida': self.concluida
				}

class Turma(Disciplina):
	""" Classe Turma """

	def __init__(self, codigo=None, nome=None, ementa=None, preRequisitos=None, cargaHoraria=None, sigla=None, horario=None, professor=None, periodo=None):
		"""Inicializador"""

		Disciplina.__init__(self, codigo, nome, ementa, preRequisitos, cargaHoraria)
		self.sigla = sigla
		self.horario = horario
		self.professor = professor

	def getTurma(self):
		"""Retorna um dicionario com as informacoes referentes a turma"""

		self.preRequisitos = re.findall(r'[A-Z]{3}[0-9]{4}', self.preRequisitos)
		self.creditos = int(re.findall(r'\d+', str(self.cargaHoraria))[0])/15
		return {
				'codigo': self.codigo,
				'nome': self.nome, 
				'ementa': self.ementa, 
				'preRequisitos': self.preRequisitos, 
				'cargaHoraria': self.cargaHoraria,
				'creditos': self.creditos,
				'sigla': self.sigla,
				'horario': self.horario,
				'professor': self.professor,
				'periodo': self.periodo,
				'prioridade': self.prioridade,
				'concluida': self.concluida
				}