from app.controllers.turma import Disciplina
from app.controllers.turma import Departamento


# campus = codigo[:3]
# ref = db.reference('/disciplina/' + campus + '/' + codigo)
# disciplinas = ref.get()
# preRequisitos = re.findall(r'[A-Z]{3}[0-9]{4}', disciplinas['preRequisitos'])

# ref = db.reference('/curso/' + nomeDoCurso)
# fluxo = ref.get()
# fluxo
# {
#     1:{
#     FGA0004: OB,
#     FGA0005: OB
#     }
#     2:{

#     }
# }
# vetor = []
# for i in fluxo:
#     vetor.append(i)

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