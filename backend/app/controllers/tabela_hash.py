class hash_table:
    def __init__(self):
        self.MAX = 100000
        self.arr = [[] for i in range (self.MAX)]


    def get_hash(self,key):
        h = 0
        v = 0
        a = 31415
        b = 27183
        for char in key:
            v+= ord(char)
            a = (a * b) % (self.MAX - 1)
            h = (a * h + v) % self.MAX
        
        return h 

    def setitem(self,key,val):
        h = self.get_hash(key)
        
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key,val)
                found = True
                break
        
        if not found:
            self.arr[h].append((key,val))

    def getitem(self, key):
        h = self.get_hash(key)
        
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def delitem(self,key):
        h = self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]

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

	def getDisciplina(self):
		"""Retorna um dicionario com as informacoes referentes a disciplina"""

		return {
				'codigo': self.codigo,
				'nome': self.nome, 
				'ementa': self.ementa, 
				'preRequisitos': self.preRequisitos, 
				'cargaHoraria': self.cargaHoraria 
				}

t = hash_table()
d=Disciplina('FGA', 'MDS', 'nada por enquanto', 'OO', 6)
t.setitem(d.nome, d)


x = t.getitem(d.nome)
print(t.get_hash(d.nome))
print(d.nome)


