class Graph:

    def __init__(self, v):
        self.V = v
        self.listaVertices = []
        self.numV = 0
        self.adj = []
        self.tc = []

        for i in range(self.V):
            self.adj.append([0] * self.V)
            self.tc.append([0] * self.V)

    def adicionaVertice(self, vertice):
        self.numV += 1
        self.listaVertices.append(vertice)

    def getindex(self, nome):
        for i in range(self.numV):
            if nome == self.listaVertices[i].nome:
                break
            else:
                i = -1

        return i

    def adicionaAresta(self, inicio, fim):
        self.adj[fim][inicio] = 1

    def Gerartc(self):
        for i in range(self.numV):
            for j in range(self.numV):
                self.tc[i][j] = self.adj[i][j]

        for i in range(self.numV):
            self.tc[i][i] = 1

        for i in range(self.numV):
            for s in range(self.numV):
                if self.tc[s][i] == 1:
                    for t in range(self.numV):
                        if self.tc[i][t] == 1:
                            self.tc[s][t] = 1

    def geradorGrauTrancamento(self):
        for i in range(self.numV):
            aux = 0
            for j in range(self.numV):
                if self.tc[j][i] == 1:
                    aux += 1

            self.listaVertices[i].grauTrancamento = aux


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
        self.grauTrancamento = 0

    

    def getDisciplina(self):
        """Retorna um dicionario com as informacoes referentes a disciplina"""

        return {
            'codigo': self.codigo,
            'nome': self.nome,
            'ementa': self.ementa,
            'preRequisitos': self.preRequisitos,
            'cargaHoraria': self.cargaHoraria
        }


d = []
d.append(Disciplina(0, '0', 'sem', '', 0))
d.append(Disciplina(0, '1', 'sem', '0', 0))
d.append(Disciplina(0, '2', 'sem', '0', 0))
d.append(Disciplina(0, '3', 'sem', '1', 0))
d.append(Disciplina(0, '4', 'sem', '1', 0))
d.append(Disciplina(0, '5', 'sem', '3', 0))
d.append(Disciplina(0, '6', 'sem', '3', 0))
d.append(Disciplina(0, '7', 'sem', '6', 0))
d.append(Disciplina(0, '8', 'sem', '6', 0))
d.append(Disciplina(0, '9', 'sem', '2', 0))
d.append(Disciplina(0, '10', 'sem', '2', 0))
d.append(Disciplina(0, '11', 'sem', '', 0))
d.append(Disciplina(0, '12', 'sem', '11', 0))
d.append(Disciplina(0, '13', 'sem', '11', 0))
d.append(Disciplina(0, '14', 'sem', '13', 0))

T = Graph(15)

for i in range(15):
    T.adicionaVertice(d[i])

for i in range(15):
    print(T.getindex(T.listaVertices[i].preRequisitos))

for i in range(15):
    if T.getindex(T.listaVertices[i].preRequisitos) != -1:
        x = T.getindex(T.listaVertices[i].preRequisitos)
        y = T.getindex(T.listaVertices[i].nome)
        T.adicionaAresta(x, y)


T.Gerartc()


for linha in T.tc:
    for coluna in linha:
        print(coluna, end=" ")
    print()

print()
print()
T.geradorGrauTrancamento()

for i in range(T.numV):
    print(T.listaVertices[i].nome, end="  ")
    print(T.listaVertices[i].grauTrancamento)
